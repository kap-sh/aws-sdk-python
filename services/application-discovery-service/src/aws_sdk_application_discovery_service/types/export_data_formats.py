"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportDataFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.export_data_format

ExportDataFormats: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.export_data_format.ExportDataFormat"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportDataFormats) -> list:
    import aws_sdk_application_discovery_service.types.export_data_format

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.export_data_format.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExportDataFormats:
    import aws_sdk_application_discovery_service.types.export_data_format

    out: ExportDataFormats = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.export_data_format.deserialize_aws_json_1_1(
                item
            )
        )
    return out
