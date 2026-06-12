"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceMetadataEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_metadata_entry

ContainerServiceMetadataEntryList: TypeAlias = list[
    "aws_sdk_lightsail.types.container_service_metadata_entry.ContainerServiceMetadataEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceMetadataEntryList) -> list:
    import aws_sdk_lightsail.types.container_service_metadata_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.container_service_metadata_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServiceMetadataEntryList:
    import aws_sdk_lightsail.types.container_service_metadata_entry

    out: ContainerServiceMetadataEntryList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.container_service_metadata_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
