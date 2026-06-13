"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashBaseUrls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.dash_base_url

DashBaseUrls: TypeAlias = list["aws_sdk_mediapackagev2.types.dash_base_url.DashBaseUrl"]


# --- restJson1 ser/de ---
def serialize_json(value: DashBaseUrls) -> list:
    import aws_sdk_mediapackagev2.types.dash_base_url

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackagev2.types.dash_base_url.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashBaseUrls:
    import aws_sdk_mediapackagev2.types.dash_base_url

    out: DashBaseUrls = []
    for item in data:
        out.append(aws_sdk_mediapackagev2.types.dash_base_url.deserialize_json(item))
    return out
