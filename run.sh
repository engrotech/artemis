pytest -v schema-testing.py --tb=short --workers 4 --html=reports/report.html --css=highcontrast.css
pytest -v schema-testing-neg.py --tb=short --workers 4 --html=reports/report-neg.html --css=highcontrast.css
