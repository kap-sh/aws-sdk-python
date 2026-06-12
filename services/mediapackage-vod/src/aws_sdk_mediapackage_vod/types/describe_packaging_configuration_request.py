"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DescribePackagingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string


class DescribePackagingConfigurationRequest(TypedDict):
    id: "aws_sdk_mediapackage_vod.types.__string.__string"
    """The ID of a MediaPackage VOD PackagingConfiguration resource."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePackagingConfigurationRequest:
    out: DescribePackagingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
