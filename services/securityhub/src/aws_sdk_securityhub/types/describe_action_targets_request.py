"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeActionTargetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.arn_list
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class DescribeActionTargetsRequest(TypedDict):
    action_target_arns: NotRequired["aws_sdk_securityhub.types.arn_list.ArnList"]
    """<p>A list of custom action target ARNs for the custom action targets to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>DescribeActionTargets</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActionTargetsRequest) -> dict:
    out: dict = {}
    if "action_target_arns" in value:
        import aws_sdk_securityhub.types.arn_list

        out["ActionTargetArns"] = aws_sdk_securityhub.types.arn_list.serialize_json(
            value["action_target_arns"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeActionTargetsRequest:
    out: DescribeActionTargetsRequest = {}  # type: ignore[typeddict-item]
    if "ActionTargetArns" in data:
        import aws_sdk_securityhub.types.arn_list

        out["action_target_arns"] = aws_sdk_securityhub.types.arn_list.deserialize_json(
            data["ActionTargetArns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
