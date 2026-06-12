"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.export_filter

ExportFilters: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.export_filter.ExportFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportFilters) -> list:
    import aws_sdk_application_discovery_service.types.export_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.export_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExportFilters:
    import aws_sdk_application_discovery_service.types.export_filter

    out: ExportFilters = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.export_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
