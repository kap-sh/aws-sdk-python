"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RegionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.region_metadata

RegionMetadataList: TypeAlias = list[
    "capo_sso_admin.types.region_metadata.RegionMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionMetadataList) -> list:
    import capo_sso_admin.types.region_metadata

    out: list = []
    for item in value:
        out.append(capo_sso_admin.types.region_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegionMetadataList:
    import capo_sso_admin.types.region_metadata

    out: RegionMetadataList = []
    for item in data:
        out.append(capo_sso_admin.types.region_metadata.deserialize_aws_json_1_1(item))
    return out
