"""Generated from Smithy shape ``com.amazonaws.connect#ListContactFlowModuleVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result1000
    import aws_sdk_connect.types.next_token


class ListContactFlowModuleVersionsRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: "aws_sdk_connect.types.arn.ARN"
    """<p>The identifier of the flow module.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactFlowModuleVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContactFlowModuleVersionsRequest:
    out: ListContactFlowModuleVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
