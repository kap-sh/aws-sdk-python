"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configurations_export_id

ExportIds: TypeAlias = list[
    "capo_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExportIds:
    return list(data)
