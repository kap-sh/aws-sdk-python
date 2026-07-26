"""Generated from Smithy shape ``com.amazonaws.licensemanager#MetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.metadata

MetadataList: TypeAlias = list["capo_license_manager.types.metadata.Metadata"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataList) -> list:
    import capo_license_manager.types.metadata

    out: list = []
    for item in value:
        out.append(capo_license_manager.types.metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetadataList:
    import capo_license_manager.types.metadata

    out: MetadataList = []
    for item in data:
        out.append(capo_license_manager.types.metadata.deserialize_aws_json_1_1(item))
    return out
