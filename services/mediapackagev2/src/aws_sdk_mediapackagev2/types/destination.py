"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.s3_destination_config


class Destination(TypedDict):
    s3_destination: (
        "aws_sdk_mediapackagev2.types.s3_destination_config.S3DestinationConfig"
    )
    """<p>The configuration for exporting harvested content to an S3 bucket. This includes details such as the bucket name and destination path within the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    import aws_sdk_mediapackagev2.types.s3_destination_config

    out["S3Destination"] = (
        aws_sdk_mediapackagev2.types.s3_destination_config.serialize_json(
            value["s3_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "S3Destination" in data:
        import aws_sdk_mediapackagev2.types.s3_destination_config

        out["s3_destination"] = (
            aws_sdk_mediapackagev2.types.s3_destination_config.deserialize_json(
                data["S3Destination"]
            )
        )
    else:
        raise DeserializationError("Destination.s3_destination required")
    return out
