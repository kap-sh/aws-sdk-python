"""Generated from Smithy shape ``com.amazonaws.qapps#DescribeQAppPermissionsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class DescribeQAppPermissionsInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Amazon Q App for which to retrieve permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQAppPermissionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeQAppPermissionsInput:
    out: DescribeQAppPermissionsInput = {}  # type: ignore[typeddict-item]
    return out
