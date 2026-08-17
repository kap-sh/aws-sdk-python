"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LowerCaseString``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.lower_case_string_with_keys


class LowerCaseString(TypedDict, closed=True):
    with_keys: (
        "capo_cloudwatch_logs.types.lower_case_string_with_keys.LowerCaseStringWithKeys"
    )
    """<p>The array caontaining the keys of the fields to convert to lowercase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LowerCaseString) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.lower_case_string_with_keys

    out["withKeys"] = (
        capo_cloudwatch_logs.types.lower_case_string_with_keys.serialize_aws_json_1_1(
            value["with_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LowerCaseString:
    out: LowerCaseString = {}  # type: ignore[typeddict-item]
    if data.get("withKeys") is not None:
        import capo_cloudwatch_logs.types.lower_case_string_with_keys

        out["with_keys"] = (
            capo_cloudwatch_logs.types.lower_case_string_with_keys.deserialize_aws_json_1_1(
                data["withKeys"]
            )
        )
    else:
        raise DeserializationError("LowerCaseString.with_keys required")
    return out
