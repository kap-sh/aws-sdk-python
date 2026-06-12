"""Generated from Smithy shape ``com.amazonaws.inspector#TelemetryMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.telemetry_metadata

TelemetryMetadataList: TypeAlias = list[
    "aws_sdk_inspector.types.telemetry_metadata.TelemetryMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TelemetryMetadataList) -> list:
    import aws_sdk_inspector.types.telemetry_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.telemetry_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TelemetryMetadataList:
    import aws_sdk_inspector.types.telemetry_metadata

    out: TelemetryMetadataList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.telemetry_metadata.deserialize_aws_json_1_1(item)
        )
    return out
