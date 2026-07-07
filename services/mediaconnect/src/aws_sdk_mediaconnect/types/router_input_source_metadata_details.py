"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputSourceMetadataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediaconnect.types.router_input_messages
    import aws_sdk_mediaconnect.types.router_input_metadata


class RouterInputSourceMetadataDetails(TypedDict, closed=True):
    source_metadata_messages: (
        "aws_sdk_mediaconnect.types.router_input_messages.RouterInputMessages"
    )
    """<p>Collection of metadata messages associated with the router input source.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp when the metadata was last updated.</p>"""
    router_input_metadata: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_metadata.RouterInputMetadata"
    ]
    """<p>Metadata information specific to the router input configuration and state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputSourceMetadataDetails) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_input_messages

    out["sourceMetadataMessages"] = (
        aws_sdk_mediaconnect.types.router_input_messages.serialize_json(
            value["source_metadata_messages"]
        )
    )
    import aws_sdk_mediaconnect.types._prelude.timestamp

    out["timestamp"] = aws_sdk_mediaconnect.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "router_input_metadata" in value:
        import aws_sdk_mediaconnect.types.router_input_metadata

        out["routerInputMetadata"] = (
            aws_sdk_mediaconnect.types.router_input_metadata.serialize_json(
                value["router_input_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouterInputSourceMetadataDetails:
    out: RouterInputSourceMetadataDetails = {}  # type: ignore[typeddict-item]
    if "sourceMetadataMessages" in data:
        import aws_sdk_mediaconnect.types.router_input_messages

        out["source_metadata_messages"] = (
            aws_sdk_mediaconnect.types.router_input_messages.deserialize_json(
                data["sourceMetadataMessages"]
            )
        )
    else:
        raise DeserializationError(
            "RouterInputSourceMetadataDetails.source_metadata_messages required"
        )
    if "timestamp" in data:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError(
            "RouterInputSourceMetadataDetails.timestamp required"
        )
    if "routerInputMetadata" in data:
        import aws_sdk_mediaconnect.types.router_input_metadata

        out["router_input_metadata"] = (
            aws_sdk_mediaconnect.types.router_input_metadata.deserialize_json(
                data["routerInputMetadata"]
            )
        )
    return out
