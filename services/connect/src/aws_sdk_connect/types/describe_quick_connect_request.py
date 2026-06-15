"""Generated from Smithy shape ``com.amazonaws.connect#DescribeQuickConnectRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.quick_connect_id


class DescribeQuickConnectRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    quick_connect_id: "aws_sdk_connect.types.quick_connect_id.QuickConnectId"
    """<p>The identifier for the quick connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQuickConnectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeQuickConnectRequest:
    out: DescribeQuickConnectRequest = {}  # type: ignore[typeddict-item]
    return out
