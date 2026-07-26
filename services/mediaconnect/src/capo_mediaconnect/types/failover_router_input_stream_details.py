"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputStreamDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.failover_router_input_indexed_stream_details


class FailoverRouterInputStreamDetails(TypedDict, closed=True):
    source_index_zero_stream_details: "capo_mediaconnect.types.failover_router_input_indexed_stream_details.FailoverRouterInputIndexedStreamDetails"
    """<p>Configuration details for the primary source (index 0) in the failover setup.</p>"""
    source_index_one_stream_details: "capo_mediaconnect.types.failover_router_input_indexed_stream_details.FailoverRouterInputIndexedStreamDetails"
    """<p>Configuration details for the secondary source (index 1) in the failover setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputStreamDetails) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.failover_router_input_indexed_stream_details

    out["sourceIndexZeroStreamDetails"] = (
        capo_mediaconnect.types.failover_router_input_indexed_stream_details.serialize_json(
            value["source_index_zero_stream_details"]
        )
    )
    import capo_mediaconnect.types.failover_router_input_indexed_stream_details

    out["sourceIndexOneStreamDetails"] = (
        capo_mediaconnect.types.failover_router_input_indexed_stream_details.serialize_json(
            value["source_index_one_stream_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> FailoverRouterInputStreamDetails:
    out: FailoverRouterInputStreamDetails = {}  # type: ignore[typeddict-item]
    if "sourceIndexZeroStreamDetails" in data:
        import capo_mediaconnect.types.failover_router_input_indexed_stream_details

        out["source_index_zero_stream_details"] = (
            capo_mediaconnect.types.failover_router_input_indexed_stream_details.deserialize_json(
                data["sourceIndexZeroStreamDetails"]
            )
        )
    else:
        raise DeserializationError(
            "FailoverRouterInputStreamDetails.source_index_zero_stream_details required"
        )
    if "sourceIndexOneStreamDetails" in data:
        import capo_mediaconnect.types.failover_router_input_indexed_stream_details

        out["source_index_one_stream_details"] = (
            capo_mediaconnect.types.failover_router_input_indexed_stream_details.deserialize_json(
                data["sourceIndexOneStreamDetails"]
            )
        )
    else:
        raise DeserializationError(
            "FailoverRouterInputStreamDetails.source_index_one_stream_details required"
        )
    return out
