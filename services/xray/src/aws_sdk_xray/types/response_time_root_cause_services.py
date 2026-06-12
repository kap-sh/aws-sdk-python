"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauseServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.response_time_root_cause_service

ResponseTimeRootCauseServices: TypeAlias = list[
    "aws_sdk_xray.types.response_time_root_cause_service.ResponseTimeRootCauseService"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauseServices) -> list:
    import aws_sdk_xray.types.response_time_root_cause_service

    out: list = []
    for item in value:
        out.append(
            aws_sdk_xray.types.response_time_root_cause_service.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResponseTimeRootCauseServices:
    import aws_sdk_xray.types.response_time_root_cause_service

    out: ResponseTimeRootCauseServices = []
    for item in data:
        out.append(
            aws_sdk_xray.types.response_time_root_cause_service.deserialize_json(item)
        )
    return out
