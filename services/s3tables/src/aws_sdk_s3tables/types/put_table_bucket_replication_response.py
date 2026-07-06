"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.version_token


class PutTableBucketReplicationResponse(TypedDict, closed=True):
    version_token: "aws_sdk_s3tables.types.version_token.VersionToken"
    """<p>A new version token representing the updated replication configuration.</p>"""
    status: "str"
    """<p>The status of the replication configuration operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketReplicationResponse) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> PutTableBucketReplicationResponse:
    out: PutTableBucketReplicationResponse = {}  # type: ignore[typeddict-item]
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    else:
        raise DeserializationError(
            "PutTableBucketReplicationResponse.version_token required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("PutTableBucketReplicationResponse.status required")
    return out
