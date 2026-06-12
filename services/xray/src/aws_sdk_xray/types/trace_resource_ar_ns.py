"""Generated from Smithy shape ``com.amazonaws.xray#TraceResourceARNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.resource_arn_detail

TraceResourceARNs: TypeAlias = list[
    "aws_sdk_xray.types.resource_arn_detail.ResourceARNDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: TraceResourceARNs) -> list:
    import aws_sdk_xray.types.resource_arn_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.resource_arn_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> TraceResourceARNs:
    import aws_sdk_xray.types.resource_arn_detail

    out: TraceResourceARNs = []
    for item in data:
        out.append(aws_sdk_xray.types.resource_arn_detail.deserialize_json(item))
    return out
