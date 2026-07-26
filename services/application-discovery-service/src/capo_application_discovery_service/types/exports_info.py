"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportsInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.export_info

ExportsInfo: TypeAlias = list[
    "capo_application_discovery_service.types.export_info.ExportInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportsInfo) -> list:
    import capo_application_discovery_service.types.export_info

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.export_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExportsInfo:
    import capo_application_discovery_service.types.export_info

    out: ExportsInfo = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.export_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
