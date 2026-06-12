"""Generated from Smithy shape ``com.amazonaws.xray#TelemetryRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.telemetry_record

TelemetryRecordList: TypeAlias = list[
    "aws_sdk_xray.types.telemetry_record.TelemetryRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRecordList) -> list:
    import aws_sdk_xray.types.telemetry_record

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.telemetry_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> TelemetryRecordList:
    import aws_sdk_xray.types.telemetry_record

    out: TelemetryRecordList = []
    for item in data:
        out.append(aws_sdk_xray.types.telemetry_record.deserialize_json(item))
    return out
