"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#EgressEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string


class EgressEndpoint(TypedDict, closed=True):
    packaging_configuration_id: NotRequired[
        "aws_sdk_mediapackage_vod.types.__string.__string"
    ]
    """The ID of the PackagingConfiguration being applied to the Asset."""
    status: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The current processing status of the asset used for the packaging configuration. The status can be either QUEUED, PROCESSING, PLAYABLE, or FAILED. Status information won't be available for most assets ingested before 2021-09-30."""
    url: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The URL of the parent manifest for the repackaged Asset."""


# --- restJson1 ser/de ---
def serialize_json(value: EgressEndpoint) -> dict:
    out: dict = {}
    if "packaging_configuration_id" in value:
        out["packagingConfigurationId"] = value["packaging_configuration_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> EgressEndpoint:
    out: EgressEndpoint = {}  # type: ignore[typeddict-item]
    if "packagingConfigurationId" in data:
        out["packaging_configuration_id"] = data["packagingConfigurationId"]
    if "status" in data:
        out["status"] = data["status"]
    if "url" in data:
        out["url"] = data["url"]
    return out
