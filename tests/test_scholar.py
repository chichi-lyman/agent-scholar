from src.agent import ScholarAgent
def test_scholar_playbook():
    p = ScholarAgent().synthesize("onboarding")
    assert len(p.steps) >= 1
