"""Generated from Smithy shape ``com.amazonaws.kendra#SiteMapsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.site_map

SiteMapsList: TypeAlias = list["aws_sdk_kendra.types.site_map.SiteMap"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SiteMapsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SiteMapsList:
    return list(data)
