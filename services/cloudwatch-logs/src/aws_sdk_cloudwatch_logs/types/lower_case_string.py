"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LowerCaseString``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.lower_case_string_with_keys


class LowerCaseString(TypedDict):
    with_keys: "aws_sdk_cloudwatch_logs.types.lower_case_string_with_keys.LowerCaseStringWithKeys"
    """<p>The array caontaining the keys of the fields to convert to lowercase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LowerCaseString) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.lower_case_string_with_keys

    out["withKeys"] = (
        aws_sdk_cloudwatch_logs.types.lower_case_string_with_keys.serialize_aws_json_1_1(
            value["with_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LowerCaseString:
    out: LowerCaseString = {}  # type: ignore[typeddict-item]
    if "withKeys" in data:
        import aws_sdk_cloudwatch_logs.types.lower_case_string_with_keys

        out["with_keys"] = (
            aws_sdk_cloudwatch_logs.types.lower_case_string_with_keys.deserialize_aws_json_1_1(
                data["withKeys"]
            )
        )
    else:
        raise DeserializationError("LowerCaseString.with_keys required")
    return out
