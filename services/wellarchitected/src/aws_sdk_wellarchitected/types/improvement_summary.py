"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImprovementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice_improvement_plans
    import aws_sdk_wellarchitected.types.improvement_plan_url
    import aws_sdk_wellarchitected.types.jira_configuration
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.question_title
    import aws_sdk_wellarchitected.types.risk


class ImprovementSummary(TypedDict, closed=True):
    question_id: NotRequired["aws_sdk_wellarchitected.types.question_id.QuestionId"]
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    question_title: NotRequired[
        "aws_sdk_wellarchitected.types.question_title.QuestionTitle"
    ]
    risk: NotRequired["aws_sdk_wellarchitected.types.risk.Risk"]
    improvement_plan_url: NotRequired[
        "aws_sdk_wellarchitected.types.improvement_plan_url.ImprovementPlanUrl"
    ]
    improvement_plans: NotRequired[
        "aws_sdk_wellarchitected.types.choice_improvement_plans.ChoiceImprovementPlans"
    ]
    """<p>The improvement plan details.</p>"""
    jira_configuration: NotRequired[
        "aws_sdk_wellarchitected.types.jira_configuration.JiraConfiguration"
    ]
    """<p>Configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImprovementSummary) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "question_title" in value:
        out["QuestionTitle"] = value["question_title"]
    if "risk" in value:
        import aws_sdk_wellarchitected.types.risk

        out["Risk"] = aws_sdk_wellarchitected.types.risk.serialize_json(value["risk"])
    if "improvement_plan_url" in value:
        out["ImprovementPlanUrl"] = value["improvement_plan_url"]
    if "improvement_plans" in value:
        import aws_sdk_wellarchitected.types.choice_improvement_plans

        out["ImprovementPlans"] = (
            aws_sdk_wellarchitected.types.choice_improvement_plans.serialize_json(
                value["improvement_plans"]
            )
        )
    if "jira_configuration" in value:
        import aws_sdk_wellarchitected.types.jira_configuration

        out["JiraConfiguration"] = (
            aws_sdk_wellarchitected.types.jira_configuration.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImprovementSummary:
    out: ImprovementSummary = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "QuestionTitle" in data:
        out["question_title"] = data["QuestionTitle"]
    if "Risk" in data:
        import aws_sdk_wellarchitected.types.risk

        out["risk"] = aws_sdk_wellarchitected.types.risk.deserialize_json(data["Risk"])
    if "ImprovementPlanUrl" in data:
        out["improvement_plan_url"] = data["ImprovementPlanUrl"]
    if "ImprovementPlans" in data:
        import aws_sdk_wellarchitected.types.choice_improvement_plans

        out["improvement_plans"] = (
            aws_sdk_wellarchitected.types.choice_improvement_plans.deserialize_json(
                data["ImprovementPlans"]
            )
        )
    if "JiraConfiguration" in data:
        import aws_sdk_wellarchitected.types.jira_configuration

        out["jira_configuration"] = (
            aws_sdk_wellarchitected.types.jira_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
