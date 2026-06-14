"""Generated from Smithy shape ``com.amazonaws.connect#DescribeUserHierarchyStructureRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id


class DescribeUserHierarchyStructureRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserHierarchyStructureRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeUserHierarchyStructureRequest:
    out: DescribeUserHierarchyStructureRequest = {}  # type: ignore[typeddict-item]
    return out
