"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportsInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.export_info

ExportsInfo: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.export_info.ExportInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportsInfo) -> list:
    import aws_sdk_application_discovery_service.types.export_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.export_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExportsInfo:
    import aws_sdk_application_discovery_service.types.export_info

    out: ExportsInfo = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.export_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
