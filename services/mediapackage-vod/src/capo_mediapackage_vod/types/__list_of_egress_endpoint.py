"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__listOfEgressEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.egress_endpoint

__listOfEgressEndpoint: TypeAlias = list[
    "capo_mediapackage_vod.types.egress_endpoint.EgressEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEgressEndpoint) -> list:
    import capo_mediapackage_vod.types.egress_endpoint

    out: list = []
    for item in value:
        out.append(capo_mediapackage_vod.types.egress_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfEgressEndpoint:
    import capo_mediapackage_vod.types.egress_endpoint

    out: __listOfEgressEndpoint = []
    for item in data:
        out.append(capo_mediapackage_vod.types.egress_endpoint.deserialize_json(item))
    return out
