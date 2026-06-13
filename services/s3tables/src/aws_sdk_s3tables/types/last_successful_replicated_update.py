"""Generated from Smithy shape ``com.amazonaws.s3tables#LastSuccessfulReplicatedUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_s3tables.types.metadata_location


class LastSuccessfulReplicatedUpdate(TypedDict):
    metadata_location: "aws_sdk_s3tables.types.metadata_location.MetadataLocation"
    """<p>The S3 location of the metadata that was successfully replicated.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp when the replication update completed successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastSuccessfulReplicatedUpdate) -> dict:
    out: dict = {}
    out["metadataLocation"] = value["metadata_location"]
    import aws_sdk_s3tables.types._prelude.timestamp

    out["timestamp"] = aws_sdk_s3tables.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    return out


def deserialize_json(data: dict) -> LastSuccessfulReplicatedUpdate:
    out: LastSuccessfulReplicatedUpdate = {}  # type: ignore[typeddict-item]
    if "metadataLocation" in data:
        out["metadata_location"] = data["metadataLocation"]
    else:
        raise DeserializationError(
            "LastSuccessfulReplicatedUpdate.metadata_location required"
        )
    if "timestamp" in data:
        import aws_sdk_s3tables.types._prelude.timestamp

        out["timestamp"] = aws_sdk_s3tables.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("LastSuccessfulReplicatedUpdate.timestamp required")
    return out
