"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CopyValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.overwrite_if_exists
    import aws_sdk_cloudwatch_logs.types.source
    import aws_sdk_cloudwatch_logs.types.target


class CopyValueEntry(TypedDict, closed=True):
    source: "aws_sdk_cloudwatch_logs.types.source.Source"
    """<p>The key to copy.</p>"""
    target: "aws_sdk_cloudwatch_logs.types.target.Target"
    """<p>The key of the field to copy the value to.</p>"""
    overwrite_if_exists: (
        "aws_sdk_cloudwatch_logs.types.overwrite_if_exists.OverwriteIfExists"
    )
    """<p>Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyValueEntry) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["target"] = value["target"]
    out["overwriteIfExists"] = value.get("overwrite_if_exists", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyValueEntry:
    out: CopyValueEntry = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("CopyValueEntry.source required")
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError("CopyValueEntry.target required")
    if "overwriteIfExists" in data:
        out["overwrite_if_exists"] = data["overwriteIfExists"]
    else:
        out["overwrite_if_exists"] = False
    return out
