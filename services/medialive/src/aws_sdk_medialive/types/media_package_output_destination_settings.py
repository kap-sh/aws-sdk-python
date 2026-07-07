"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageOutputDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_min1


class MediaPackageOutputDestinationSettings(TypedDict, closed=True):
    channel_id: NotRequired["aws_sdk_medialive.types.__string_min1.__stringMin1"]
    """ID of the channel in MediaPackage that is the destination for this output group. You do not need to specify the individual inputs in MediaPackage; MediaLive will handle the connection of the two MediaLive pipelines to the two MediaPackage inputs. The MediaPackage channel and MediaLive channel must be in the same region."""
    channel_group: NotRequired["aws_sdk_medialive.types.__string_min1.__stringMin1"]
    """Name of the channel group in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2."""
    channel_name: NotRequired["aws_sdk_medialive.types.__string_min1.__stringMin1"]
    """Name of the channel in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2."""
    channel_endpoint_id: NotRequired[
        "aws_sdk_medialive.types.__string_min1.__stringMin1"
    ]
    """Endpoint 1 or 2 of the channel in MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2."""
    media_package_region_name: NotRequired[
        "aws_sdk_medialive.types.__string_min1.__stringMin1"
    ]
    """Region the channel group and channel are located in for MediaPackageV2. Only use if you are sending CMAF Ingest output to a CMAF ingest endpoint on a MediaPackage channel that uses MediaPackage v2."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageOutputDestinationSettings) -> dict:
    out: dict = {}
    if "channel_id" in value:
        out["channelId"] = value["channel_id"]
    if "channel_group" in value:
        out["channelGroup"] = value["channel_group"]
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    if "channel_endpoint_id" in value:
        out["channelEndpointId"] = value["channel_endpoint_id"]
    if "media_package_region_name" in value:
        out["mediaPackageRegionName"] = value["media_package_region_name"]
    return out


def deserialize_json(data: dict) -> MediaPackageOutputDestinationSettings:
    out: MediaPackageOutputDestinationSettings = {}  # type: ignore[typeddict-item]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    if "channelGroup" in data:
        out["channel_group"] = data["channelGroup"]
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    if "channelEndpointId" in data:
        out["channel_endpoint_id"] = data["channelEndpointId"]
    if "mediaPackageRegionName" in data:
        out["media_package_region_name"] = data["mediaPackageRegionName"]
    return out
