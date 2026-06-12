"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ContinuousExportIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configurations_export_id

ContinuousExportIds: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousExportIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ContinuousExportIds:
    return list(data)
