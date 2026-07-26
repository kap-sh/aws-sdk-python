"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CustomAdTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.custom_ad_type

CustomAdTypeList: TypeAlias = list[
    "capo_mediapackagev2.types.custom_ad_type.CustomAdType"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomAdTypeList) -> list:
    import capo_mediapackagev2.types.custom_ad_type

    out: list = []
    for item in value:
        out.append(capo_mediapackagev2.types.custom_ad_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomAdTypeList:
    import capo_mediapackagev2.types.custom_ad_type

    out: CustomAdTypeList = []
    for item in data:
        out.append(capo_mediapackagev2.types.custom_ad_type.deserialize_json(item))
    return out
