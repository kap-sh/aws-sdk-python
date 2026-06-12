"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ContinuousExportDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.continuous_export_description

ContinuousExportDescriptions: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.continuous_export_description.ContinuousExportDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousExportDescriptions) -> list:
    import aws_sdk_application_discovery_service.types.continuous_export_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.continuous_export_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContinuousExportDescriptions:
    import aws_sdk_application_discovery_service.types.continuous_export_description

    out: ContinuousExportDescriptions = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.continuous_export_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
