"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputStreamDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details


class MergeRouterInputStreamDetails(TypedDict):
    source_index_zero_stream_details: "aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details.MergeRouterInputIndexedStreamDetails"
    """<p>Configuration details for the first source (index 0) in the merge setup.</p>"""
    source_index_one_stream_details: "aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details.MergeRouterInputIndexedStreamDetails"
    """<p>Configuration details for the second source (index 1) in the merge setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputStreamDetails) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details

    out["sourceIndexZeroStreamDetails"] = (
        aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details.serialize_json(
            value["source_index_zero_stream_details"]
        )
    )
    import aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details

    out["sourceIndexOneStreamDetails"] = (
        aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details.serialize_json(
            value["source_index_one_stream_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> MergeRouterInputStreamDetails:
    out: MergeRouterInputStreamDetails = {}  # type: ignore[typeddict-item]
    if "sourceIndexZeroStreamDetails" in data:
        import aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details

        out["source_index_zero_stream_details"] = (
            aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details.deserialize_json(
                data["sourceIndexZeroStreamDetails"]
            )
        )
    else:
        raise DeserializationError(
            "MergeRouterInputStreamDetails.source_index_zero_stream_details required"
        )
    if "sourceIndexOneStreamDetails" in data:
        import aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details

        out["source_index_one_stream_details"] = (
            aws_sdk_mediaconnect.types.merge_router_input_indexed_stream_details.deserialize_json(
                data["sourceIndexOneStreamDetails"]
            )
        )
    else:
        raise DeserializationError(
            "MergeRouterInputStreamDetails.source_index_one_stream_details required"
        )
    return out
