"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TrimString``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.trim_string_with_keys


class TrimString(TypedDict, closed=True):
    with_keys: "capo_cloudwatch_logs.types.trim_string_with_keys.TrimStringWithKeys"
    """<p>The array containing the keys of the fields to trim.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrimString) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.trim_string_with_keys

    out["withKeys"] = (
        capo_cloudwatch_logs.types.trim_string_with_keys.serialize_aws_json_1_1(
            value["with_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrimString:
    out: TrimString = {}  # type: ignore[typeddict-item]
    if "withKeys" in data:
        import capo_cloudwatch_logs.types.trim_string_with_keys

        out["with_keys"] = (
            capo_cloudwatch_logs.types.trim_string_with_keys.deserialize_aws_json_1_1(
                data["withKeys"]
            )
        )
    else:
        raise DeserializationError("TrimString.with_keys required")
    return out
