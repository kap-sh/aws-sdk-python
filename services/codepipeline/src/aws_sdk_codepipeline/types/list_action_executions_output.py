"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListActionExecutionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_execution_detail_list
    import aws_sdk_codepipeline.types.next_token


class ListActionExecutionsOutput(TypedDict):
    action_execution_details: NotRequired[
        "aws_sdk_codepipeline.types.action_execution_detail_list.ActionExecutionDetailList"
    ]
    """<p>The details for a list of recent executions, such as action execution ID.</p>"""
    next_token: NotRequired["aws_sdk_codepipeline.types.next_token.NextToken"]
    """<p>If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent <code>ListActionExecutions</code> call to return the next set of action executions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActionExecutionsOutput) -> dict:
    out: dict = {}
    if "action_execution_details" in value:
        import aws_sdk_codepipeline.types.action_execution_detail_list

        out["actionExecutionDetails"] = (
            aws_sdk_codepipeline.types.action_execution_detail_list.serialize_aws_json_1_1(
                value["action_execution_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActionExecutionsOutput:
    out: ListActionExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "actionExecutionDetails" in data:
        import aws_sdk_codepipeline.types.action_execution_detail_list

        out["action_execution_details"] = (
            aws_sdk_codepipeline.types.action_execution_detail_list.deserialize_aws_json_1_1(
                data["actionExecutionDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
