"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauseEntityPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.response_time_root_cause_entity

ResponseTimeRootCauseEntityPath: TypeAlias = list[
    "aws_sdk_xray.types.response_time_root_cause_entity.ResponseTimeRootCauseEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauseEntityPath) -> list:
    import aws_sdk_xray.types.response_time_root_cause_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_xray.types.response_time_root_cause_entity.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResponseTimeRootCauseEntityPath:
    import aws_sdk_xray.types.response_time_root_cause_entity

    out: ResponseTimeRootCauseEntityPath = []
    for item in data:
        out.append(
            aws_sdk_xray.types.response_time_root_cause_entity.deserialize_json(item)
        )
    return out
