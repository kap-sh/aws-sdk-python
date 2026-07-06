"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncBlockerContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.sync_blocker_context_key
    import aws_sdk_codeconnections.types.sync_blocker_context_value


class SyncBlockerContext(TypedDict, closed=True):
    key: "aws_sdk_codeconnections.types.sync_blocker_context_key.SyncBlockerContextKey"
    """<p>The key provided for a context key-value pair for a specific sync blocker.</p>"""
    value: "aws_sdk_codeconnections.types.sync_blocker_context_value.SyncBlockerContextValue"
    """<p>The value provided for a context key-value pair for a specific sync blocker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerContext) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlockerContext:
    out: SyncBlockerContext = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("SyncBlockerContext.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("SyncBlockerContext.value required")
    return out
