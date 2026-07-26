"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesMetadata``."""

from typing_extensions import NotRequired, TypedDict


class KeyspacesMetadata(TypedDict, closed=True):
    expiration_time: NotRequired["str"]
    """<p>The time at which the associated data will expire, based on the time-to-live (TTL) setting.</p>"""
    write_time: NotRequired["str"]
    """<p>The timestamp at which the associated data was written to the database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesMetadata) -> dict:
    out: dict = {}
    if "expiration_time" in value:
        out["expirationTime"] = value["expiration_time"]
    if "write_time" in value:
        out["writeTime"] = value["write_time"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspacesMetadata:
    out: KeyspacesMetadata = {}  # type: ignore[typeddict-item]
    if "expirationTime" in data:
        out["expiration_time"] = data["expirationTime"]
    if "writeTime" in data:
        out["write_time"] = data["writeTime"]
    return out
