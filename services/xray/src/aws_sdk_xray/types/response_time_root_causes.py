"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.response_time_root_cause

ResponseTimeRootCauses: TypeAlias = list[
    "aws_sdk_xray.types.response_time_root_cause.ResponseTimeRootCause"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauses) -> list:
    import aws_sdk_xray.types.response_time_root_cause

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.response_time_root_cause.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseTimeRootCauses:
    import aws_sdk_xray.types.response_time_root_cause

    out: ResponseTimeRootCauses = []
    for item in data:
        out.append(aws_sdk_xray.types.response_time_root_cause.deserialize_json(item))
    return out
