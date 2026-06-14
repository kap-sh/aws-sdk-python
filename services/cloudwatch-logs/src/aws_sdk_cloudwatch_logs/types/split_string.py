"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SplitString``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.split_string_entries


class SplitString(TypedDict):
    entries: "aws_sdk_cloudwatch_logs.types.split_string_entries.SplitStringEntries"
    """<p>An array of <code>SplitStringEntry</code> objects, where each object contains the information about one field to split. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitString) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.split_string_entries

    out["entries"] = (
        aws_sdk_cloudwatch_logs.types.split_string_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitString:
    out: SplitString = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_cloudwatch_logs.types.split_string_entries

        out["entries"] = (
            aws_sdk_cloudwatch_logs.types.split_string_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("SplitString.entries required")
    return out
