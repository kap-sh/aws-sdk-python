"""Generated from Smithy shape ``com.amazonaws.odb#CrossRegionS3RestoreSourcesAccessList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.cross_region_s3_restore_sources_access

CrossRegionS3RestoreSourcesAccessList: TypeAlias = list[
    "aws_sdk_odb.types.cross_region_s3_restore_sources_access.CrossRegionS3RestoreSourcesAccess"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CrossRegionS3RestoreSourcesAccessList) -> list:
    import aws_sdk_odb.types.cross_region_s3_restore_sources_access

    out: list = []
    for item in value:
        out.append(
            aws_sdk_odb.types.cross_region_s3_restore_sources_access.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CrossRegionS3RestoreSourcesAccessList:
    import aws_sdk_odb.types.cross_region_s3_restore_sources_access

    out: CrossRegionS3RestoreSourcesAccessList = []
    for item in data:
        out.append(
            aws_sdk_odb.types.cross_region_s3_restore_sources_access.deserialize_aws_json_1_0(
                item
            )
        )
    return out
