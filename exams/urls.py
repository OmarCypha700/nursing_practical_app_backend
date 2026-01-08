# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     ProgramListView,
#     StudentByProgramView,
#     ProcedureByProgramView,
#     ProcedureDetailView,
#     AutosaveStepScoreView,
#     ReconciliationView,
#     SaveReconciliationView,
#     StudentDetailView,
#     DashboardStatsView,
#     ExaminerViewSet,
#     StudentViewSet,
#     ProcedureViewSet,
#     ProcedureStepViewSet,
#     ProgramViewSet,
#     StudentGradesView,
#     ExportGradesView,
#     TestGradesView,
# )

# # Create router for viewsets
# router = DefaultRouter()
# router.register(r'admin/examiners', ExaminerViewSet, basename='examiner')
# router.register(r'admin/students', StudentViewSet, basename='admin-student')
# router.register(r'admin/procedures', ProcedureViewSet, basename='admin-procedure')
# router.register(r'admin/procedure-steps', ProcedureStepViewSet, basename='admin-procedure-step')
# router.register(r'programs', ProgramViewSet, basename='program')

# urlpatterns = [
#     # Include router URLs
#     path('', include(router.urls)),
    
#     # Existing endpoints
#     path("programs/", ProgramListView.as_view()),
#     path("programs/<int:program_id>/students/", StudentByProgramView.as_view()),
#     path("programs/<int:program_id>/procedures/", ProcedureByProgramView.as_view()),
#     path("students/<int:pk>/", StudentDetailView.as_view(), name='student-detail'),
#     path("students/<int:student_id>/procedures/<int:pk>/", ProcedureDetailView.as_view()),
#     path("autosave-step-score/", AutosaveStepScoreView.as_view()),
    
#     # Reconciliation
#     path("students/<int:student_id>/procedures/<int:procedure_id>/reconciliation/", 
#          ReconciliationView.as_view(), name='reconciliation'),
#     path("save-reconciliation/", SaveReconciliationView.as_view(), name='save-reconciliation'),
    
#     # Dashboard
#     path("admin/dashboard-stats/", DashboardStatsView.as_view(), name='dashboard-stats'),

#     # Grades
#     path("admin/grades/", StudentGradesView.as_view(), name='student-grades'),
#     path("admin/grades/export/", ExportGradesView.as_view(), name='export-grades'),
#     path("admin/grades/test/", TestGradesView.as_view()),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProgramListView,
    StudentByProgramView,
    ProcedureByProgramView,
    ProcedureDetailView,
    AutosaveStepScoreView,
    ReconciliationView,
    SaveReconciliationView,
    StudentDetailView,
    DashboardStatsView,
    ExaminerViewSet,
    StudentViewSet,
    ProcedureViewSet,
    ProcedureStepViewSet,
    StudentGradesView,
    # ExportGradesView,
    # ExportStudentsView,
    ImportStudentsView,
    DownloadStudentTemplateView,
    ImportProceduresView,
    DownloadProcedureTemplateView,
)

# Router for viewsets
router = DefaultRouter()
router.register(r'admin/examiners', ExaminerViewSet, basename='examiner')
router.register(r'admin/students', StudentViewSet, basename='admin-student')
router.register(r'admin/procedures', ProcedureViewSet, basename='admin-procedure')
router.register(r'admin/procedure-steps', ProcedureStepViewSet, basename='admin-procedure-step')

urlpatterns = [
    # Standard endpoints (BEFORE router)
    path("programs/", ProgramListView.as_view()),
    path("programs/<int:program_id>/students/", StudentByProgramView.as_view()),
    path("programs/<int:program_id>/procedures/", ProcedureByProgramView.as_view()),
    path("students/<int:pk>/", StudentDetailView.as_view()),
    path("students/<int:student_id>/procedures/<int:pk>/", ProcedureDetailView.as_view()),
    path("autosave-step-score/", AutosaveStepScoreView.as_view()),

    # Student import/export
    path("students/import/", ImportStudentsView.as_view(), name='import-students'),
    path("students/template/", DownloadStudentTemplateView.as_view(), name='student-template'),
    
    # Reconciliation
    path("students/<int:student_id>/procedures/<int:procedure_id>/reconciliation/", 
         ReconciliationView.as_view()),
    path("save-reconciliation/", SaveReconciliationView.as_view()),
    
    # Admin dashboard
    path("dashboard-stats/", DashboardStatsView.as_view()),
    
    # Grades
    path("grades/", StudentGradesView.as_view(), name='student-grades'),

    # Procedure import/template
    path("procedures/import/", ImportProceduresView.as_view(), name='import-procedures'),
    path("procedures/template/", DownloadProcedureTemplateView.as_view(), name='procedure-template'),
    
    # Router URLs LAST
    path('', include(router.urls)),
]