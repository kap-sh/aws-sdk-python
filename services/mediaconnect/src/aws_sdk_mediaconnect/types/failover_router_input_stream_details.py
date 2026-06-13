"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputStreamDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details


class FailoverRouterInputStreamDetails(TypedDict):
    source_index_zero_stream_details: "aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details.FailoverRouterInputIndexedStreamDetails"
    """<p>Configuration details for the primary source (index 0) in the failover setup.</p>"""
    source_index_one_stream_details: "aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details.FailoverRouterInputIndexedStreamDetails"
    """<p>Configuration details for the secondary source (index 1) in the failover setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputStreamDetails) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details

    out["sourceIndexZeroStreamDetails"] = (
        aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details.serialize_json(
            value["source_index_zero_stream_details"]
        )
    )
    import aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details

    out["sourceIndexOneStreamDetails"] = (
        aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details.serialize_json(
            value["source_index_one_stream_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> FailoverRouterInputStreamDetails:
    out: FailoverRouterInputStreamDetails = {}  # type: ignore[typeddict-item]
    if "sourceIndexZeroStreamDetails" in data:
        import aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details

        out["source_index_zero_stream_details"] = (
            aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details.deserialize_json(
                data["sourceIndexZeroStreamDetails"]
            )
        )
    else:
        raise DeserializationError(
            "FailoverRouterInputStreamDetails.source_index_zero_stream_details required"
        )
    if "sourceIndexOneStreamDetails" in data:
        import aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details

        out["source_index_one_stream_details"] = (
            aws_sdk_mediaconnect.types.failover_router_input_indexed_stream_details.deserialize_json(
                data["sourceIndexOneStreamDetails"]
            )
        )
    else:
        raise DeserializationError(
            "FailoverRouterInputStreamDetails.source_index_one_stream_details required"
        )
    return out
