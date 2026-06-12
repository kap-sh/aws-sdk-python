"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RenameKeyEntry``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.key
    import aws_sdk_cloudwatch_logs.types.overwrite_if_exists
    import aws_sdk_cloudwatch_logs.types.rename_to


class RenameKeyEntry(TypedDict):
    key: "aws_sdk_cloudwatch_logs.types.key.Key"
    """<p>The key to rename</p>"""
    rename_to: "aws_sdk_cloudwatch_logs.types.rename_to.RenameTo"
    """<p>The string to use for the new key name</p>"""
    overwrite_if_exists: (
        "aws_sdk_cloudwatch_logs.types.overwrite_if_exists.OverwriteIfExists"
    )
    """<p>Specifies whether to overwrite the existing value if the destination key already exists. The default is <code>false</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenameKeyEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["renameTo"] = value["rename_to"]
    out["overwriteIfExists"] = value.get("overwrite_if_exists", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RenameKeyEntry:
    out: RenameKeyEntry = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("RenameKeyEntry.key required")
    if "renameTo" in data:
        out["rename_to"] = data["renameTo"]
    else:
        raise DeserializationError("RenameKeyEntry.rename_to required")
    if "overwriteIfExists" in data:
        out["overwrite_if_exists"] = data["overwriteIfExists"]
    else:
        out["overwrite_if_exists"] = False
    return out
