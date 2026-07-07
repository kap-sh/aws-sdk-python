"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableReplicationResponse``."""

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError


class PutTableReplicationResponse(TypedDict, closed=True):
    version_token: "str"
    """<p>A new version token representing the updated replication configuration.</p>"""
    status: "str"
    """<p>The status of the replication configuration operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableReplicationResponse) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> PutTableReplicationResponse:
    out: PutTableReplicationResponse = {}  # type: ignore[typeddict-item]
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    else:
        raise DeserializationError("PutTableReplicationResponse.version_token required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("PutTableReplicationResponse.status required")
    return out
