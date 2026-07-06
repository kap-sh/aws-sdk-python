"""Generated from Smithy shape ``com.amazonaws.textract#NormalizedValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.string
    import aws_sdk_textract.types.value_type


class NormalizedValue(TypedDict, closed=True):
    value: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The value of the date, written as Year-Month-DayTHour:Minute:Second.</p>"""
    value_type: NotRequired["aws_sdk_textract.types.value_type.ValueType"]
    """<p>The normalized type of the value detected. In this case, DATE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NormalizedValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "value_type" in value:
        import aws_sdk_textract.types.value_type

        out["ValueType"] = aws_sdk_textract.types.value_type.serialize_aws_json_1_1(
            value["value_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NormalizedValue:
    out: NormalizedValue = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "ValueType" in data:
        import aws_sdk_textract.types.value_type

        out["value_type"] = aws_sdk_textract.types.value_type.deserialize_aws_json_1_1(
            data["ValueType"]
        )
    return out
