"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ContinuousExportDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.continuous_export_description

ContinuousExportDescriptions: TypeAlias = list[
    "capo_application_discovery_service.types.continuous_export_description.ContinuousExportDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousExportDescriptions) -> list:
    import capo_application_discovery_service.types.continuous_export_description

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.continuous_export_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContinuousExportDescriptions:
    import capo_application_discovery_service.types.continuous_export_description

    out: ContinuousExportDescriptions = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.continuous_export_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
