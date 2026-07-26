"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceMetadataEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_metadata_entry

ContainerServiceMetadataEntryList: TypeAlias = list[
    "capo_lightsail.types.container_service_metadata_entry.ContainerServiceMetadataEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceMetadataEntryList) -> list:
    import capo_lightsail.types.container_service_metadata_entry

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.container_service_metadata_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServiceMetadataEntryList:
    import capo_lightsail.types.container_service_metadata_entry

    out: ContainerServiceMetadataEntryList = []
    for item in data:
        out.append(
            capo_lightsail.types.container_service_metadata_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
