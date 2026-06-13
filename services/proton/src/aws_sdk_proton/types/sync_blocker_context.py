"""Generated from Smithy shape ``com.amazonaws.proton#SyncBlockerContext``."""

from typing import TypedDict

from aws_sdk_proton.errors import DeserializationError


class SyncBlockerContext(TypedDict):
    key: "str"
    """<p>The key for the sync blocker context.</p>"""
    value: "str"
    """<p>The value of the sync blocker context.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerContext) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlockerContext:
    out: SyncBlockerContext = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("SyncBlockerContext.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SyncBlockerContext.value required")
    return out
