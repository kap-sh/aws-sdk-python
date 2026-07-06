"""Generated from Smithy shape ``com.amazonaws.inspector#ListAssessmentRunAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_agent_list
    import aws_sdk_inspector.types.pagination_token


class ListAssessmentRunAgentsResponse(TypedDict, closed=True):
    assessment_run_agents: (
        "aws_sdk_inspector.types.assessment_run_agent_list.AssessmentRunAgentList"
    )
    """<p>A list of ARNs that specifies the agents returned by the action.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p> When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the <b>nextToken</b> parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssessmentRunAgentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.assessment_run_agent_list

    out["assessmentRunAgents"] = (
        aws_sdk_inspector.types.assessment_run_agent_list.serialize_aws_json_1_1(
            value["assessment_run_agents"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssessmentRunAgentsResponse:
    out: ListAssessmentRunAgentsResponse = {}  # type: ignore[typeddict-item]
    if "assessmentRunAgents" in data:
        import aws_sdk_inspector.types.assessment_run_agent_list

        out["assessment_run_agents"] = (
            aws_sdk_inspector.types.assessment_run_agent_list.deserialize_aws_json_1_1(
                data["assessmentRunAgents"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssessmentRunAgentsResponse.assessment_run_agents required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
