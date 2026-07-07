"""Generated from Smithy shape ``com.amazonaws.iot#ListSecurityProfilesForTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.recursive
    import aws_sdk_iot.types.security_profile_target_arn


class ListSecurityProfilesForTargetRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    recursive: "aws_sdk_iot.types.recursive.Recursive"
    """<p>If true, return child groups too.</p>"""
    security_profile_target_arn: (
        "aws_sdk_iot.types.security_profile_target_arn.SecurityProfileTargetArn"
    )
    """<p>The ARN of the target (thing group) whose attached security profiles you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilesForTargetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSecurityProfilesForTargetRequest:
    out: ListSecurityProfilesForTargetRequest = {}  # type: ignore[typeddict-item]
    return out
