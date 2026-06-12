"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListTargetsByRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.next_token
    import aws_sdk_cloudwatch_events.types.target_list


class ListTargetsByRuleResponse(TypedDict):
    targets: NotRequired["aws_sdk_cloudwatch_events.types.target_list.TargetList"]
    """<p>The targets assigned to the rule.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>Indicates whether there are additional results to retrieve. If there are no more results, the value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTargetsByRuleResponse) -> dict:
    out: dict = {}
    if "targets" in value:
        import aws_sdk_cloudwatch_events.types.target_list

        out["Targets"] = (
            aws_sdk_cloudwatch_events.types.target_list.serialize_aws_json_1_1(
                value["targets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTargetsByRuleResponse:
    out: ListTargetsByRuleResponse = {}  # type: ignore[typeddict-item]
    if "Targets" in data:
        import aws_sdk_cloudwatch_events.types.target_list

        out["targets"] = (
            aws_sdk_cloudwatch_events.types.target_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
