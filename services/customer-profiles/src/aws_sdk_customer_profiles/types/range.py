"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Range``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.unit
    import aws_sdk_customer_profiles.types.value
    import aws_sdk_customer_profiles.types.value_range


class Range(TypedDict, closed=True):
    value: "aws_sdk_customer_profiles.types.value.Value"
    """<p>The amount of time of the specified unit.</p>"""
    unit: "aws_sdk_customer_profiles.types.unit.Unit"
    """<p>The unit of time.</p>"""
    value_range: NotRequired["aws_sdk_customer_profiles.types.value_range.ValueRange"]
    """<p>A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute. Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.</p>"""
    timestamp_source: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    r"""<p>An expression specifying the field in your JSON object from which the date should be parsed. The expression should follow the structure of \\"{ObjectTypeName.<Location of timestamp field in JSON pointer format>}\\". E.g. if your object type is MyType and source JSON is {\"generatedAt\": {\"timestamp\": \"1737587945945\"}}, then TimestampSource should be \"{MyType.generatedAt.timestamp}\".</p>"""
    timestamp_format: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    r"""<p>The format the timestamp field in your JSON object is specified. This value should be one of EPOCHMILLI (for Unix epoch timestamps with second/millisecond level precision) or ISO_8601 (following ISO_8601 format with second/millisecond level precision, with an optional offset of Z or in the format HH:MM or HHMM.). E.g. if your object type is MyType and source JSON is {\"generatedAt\": {\"timestamp\": \"2001-07-04T12:08:56.235-0700\"}}, then TimestampFormat should be \"ISO_8601\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", 0)
    import aws_sdk_customer_profiles.types.unit

    out["Unit"] = aws_sdk_customer_profiles.types.unit.serialize_json(
        value.get("unit", "DAYS")
    )
    if "value_range" in value:
        import aws_sdk_customer_profiles.types.value_range

        out["ValueRange"] = aws_sdk_customer_profiles.types.value_range.serialize_json(
            value["value_range"]
        )
    if "timestamp_source" in value:
        out["TimestampSource"] = value["timestamp_source"]
    if "timestamp_format" in value:
        out["TimestampFormat"] = value["timestamp_format"]
    return out


def deserialize_json(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if "Unit" in data:
        import aws_sdk_customer_profiles.types.unit

        out["unit"] = aws_sdk_customer_profiles.types.unit.deserialize_json(
            data["Unit"]
        )
    else:
        out["unit"] = "DAYS"
    if "ValueRange" in data:
        import aws_sdk_customer_profiles.types.value_range

        out["value_range"] = (
            aws_sdk_customer_profiles.types.value_range.deserialize_json(
                data["ValueRange"]
            )
        )
    if "TimestampSource" in data:
        out["timestamp_source"] = data["TimestampSource"]
    if "TimestampFormat" in data:
        out["timestamp_format"] = data["TimestampFormat"]
    return out
