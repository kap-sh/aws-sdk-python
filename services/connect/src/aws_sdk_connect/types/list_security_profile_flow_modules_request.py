"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityProfileFlowModulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result1000
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.security_profile_id


class ListSecurityProfileFlowModulesRequest(TypedDict):
    security_profile_id: "aws_sdk_connect.types.security_profile_id.SecurityProfileId"
    """<p> The identifier for the security profile. </p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p> The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result1000.MaxResult1000"]
    """<p> The maximum number of results to return per page. The default MaxResult size is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfileFlowModulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSecurityProfileFlowModulesRequest:
    out: ListSecurityProfileFlowModulesRequest = {}  # type: ignore[typeddict-item]
    return out
