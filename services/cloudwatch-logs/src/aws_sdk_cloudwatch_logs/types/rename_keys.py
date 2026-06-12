"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RenameKeys``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.rename_key_entries


class RenameKeys(TypedDict):
    entries: "aws_sdk_cloudwatch_logs.types.rename_key_entries.RenameKeyEntries"
    """<p>An array of <code>RenameKeyEntry</code> objects, where each object contains the information about a single key to rename. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenameKeys) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.rename_key_entries

    out["entries"] = (
        aws_sdk_cloudwatch_logs.types.rename_key_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenameKeys:
    out: RenameKeys = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_cloudwatch_logs.types.rename_key_entries

        out["entries"] = (
            aws_sdk_cloudwatch_logs.types.rename_key_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("RenameKeys.entries required")
    return out
