"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MoveKeys``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.move_key_entries


class MoveKeys(TypedDict, closed=True):
    entries: "aws_sdk_cloudwatch_logs.types.move_key_entries.MoveKeyEntries"
    """<p>An array of objects, where each object contains the information about one key to move. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MoveKeys) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.move_key_entries

    out["entries"] = (
        aws_sdk_cloudwatch_logs.types.move_key_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> MoveKeys:
    out: MoveKeys = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_cloudwatch_logs.types.move_key_entries

        out["entries"] = (
            aws_sdk_cloudwatch_logs.types.move_key_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("MoveKeys.entries required")
    return out
