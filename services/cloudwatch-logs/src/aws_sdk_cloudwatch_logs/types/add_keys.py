"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AddKeys``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.add_key_entries


class AddKeys(TypedDict):
    entries: "aws_sdk_cloudwatch_logs.types.add_key_entries.AddKeyEntries"
    """<p>An array of objects, where each object contains the information about one key to add to the log event. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddKeys) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.add_key_entries

    out["entries"] = (
        aws_sdk_cloudwatch_logs.types.add_key_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddKeys:
    out: AddKeys = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_cloudwatch_logs.types.add_key_entries

        out["entries"] = (
            aws_sdk_cloudwatch_logs.types.add_key_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("AddKeys.entries required")
    return out
