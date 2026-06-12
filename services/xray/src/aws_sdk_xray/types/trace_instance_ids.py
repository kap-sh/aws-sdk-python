"""Generated from Smithy shape ``com.amazonaws.xray#TraceInstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.instance_id_detail

TraceInstanceIds: TypeAlias = list[
    "aws_sdk_xray.types.instance_id_detail.InstanceIdDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: TraceInstanceIds) -> list:
    import aws_sdk_xray.types.instance_id_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.instance_id_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> TraceInstanceIds:
    import aws_sdk_xray.types.instance_id_detail

    out: TraceInstanceIds = []
    for item in data:
        out.append(aws_sdk_xray.types.instance_id_detail.deserialize_json(item))
    return out
