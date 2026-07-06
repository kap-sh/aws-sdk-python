"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeActionTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.action_target_list
    import aws_sdk_securityhub.types.next_token


class DescribeActionTargetsResponse(TypedDict, closed=True):
    action_targets: NotRequired[
        "aws_sdk_securityhub.types.action_target_list.ActionTargetList"
    ]
    """<p>A list of <code>ActionTarget</code> objects. Each object includes the <code>ActionTargetArn</code>, <code>Description</code>, and <code>Name</code> of a custom action target available in Security Hub CSPM.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActionTargetsResponse) -> dict:
    out: dict = {}
    if "action_targets" in value:
        import aws_sdk_securityhub.types.action_target_list

        out["ActionTargets"] = (
            aws_sdk_securityhub.types.action_target_list.serialize_json(
                value["action_targets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeActionTargetsResponse:
    out: DescribeActionTargetsResponse = {}  # type: ignore[typeddict-item]
    if "ActionTargets" in data:
        import aws_sdk_securityhub.types.action_target_list

        out["action_targets"] = (
            aws_sdk_securityhub.types.action_target_list.deserialize_json(
                data["ActionTargets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
