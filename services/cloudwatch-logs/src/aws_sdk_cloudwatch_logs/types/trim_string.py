"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TrimString``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.trim_string_with_keys


class TrimString(TypedDict):
    with_keys: "aws_sdk_cloudwatch_logs.types.trim_string_with_keys.TrimStringWithKeys"
    """<p>The array containing the keys of the fields to trim.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrimString) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.trim_string_with_keys

    out["withKeys"] = (
        aws_sdk_cloudwatch_logs.types.trim_string_with_keys.serialize_aws_json_1_1(
            value["with_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrimString:
    out: TrimString = {}  # type: ignore[typeddict-item]
    if "withKeys" in data:
        import aws_sdk_cloudwatch_logs.types.trim_string_with_keys

        out["with_keys"] = (
            aws_sdk_cloudwatch_logs.types.trim_string_with_keys.deserialize_aws_json_1_1(
                data["withKeys"]
            )
        )
    else:
        raise DeserializationError("TrimString.with_keys required")
    return out
