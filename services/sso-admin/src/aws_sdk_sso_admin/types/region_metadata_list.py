"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RegionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.region_metadata

RegionMetadataList: TypeAlias = list[
    "aws_sdk_sso_admin.types.region_metadata.RegionMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionMetadataList) -> list:
    import aws_sdk_sso_admin.types.region_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_sso_admin.types.region_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegionMetadataList:
    import aws_sdk_sso_admin.types.region_metadata

    out: RegionMetadataList = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.region_metadata.deserialize_aws_json_1_1(item)
        )
    return out
