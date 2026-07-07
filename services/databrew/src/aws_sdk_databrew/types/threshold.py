"""Generated from Smithy shape ``com.amazonaws.databrew#Threshold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.threshold_type
    import aws_sdk_databrew.types.threshold_unit
    import aws_sdk_databrew.types.threshold_value


class Threshold(TypedDict, closed=True):
    value: "aws_sdk_databrew.types.threshold_value.ThresholdValue"
    """<p>The value of a threshold.</p>"""
    type: NotRequired["aws_sdk_databrew.types.threshold_type.ThresholdType"]
    """<p>The type of a threshold. Used for comparison of an actual count of rows that satisfy the rule to the threshold value.</p>"""
    unit: NotRequired["aws_sdk_databrew.types.threshold_unit.ThresholdUnit"]
    """<p>Unit of threshold value. Can be either a COUNT or PERCENTAGE of the full sample size used for validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Threshold) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", 0)
    if "type" in value:
        import aws_sdk_databrew.types.threshold_type

        out["Type"] = aws_sdk_databrew.types.threshold_type.serialize_json(
            value["type"]
        )
    if "unit" in value:
        import aws_sdk_databrew.types.threshold_unit

        out["Unit"] = aws_sdk_databrew.types.threshold_unit.serialize_json(
            value["unit"]
        )
    return out


def deserialize_json(data: dict) -> Threshold:
    out: Threshold = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if "Type" in data:
        import aws_sdk_databrew.types.threshold_type

        out["type"] = aws_sdk_databrew.types.threshold_type.deserialize_json(
            data["Type"]
        )
    if "Unit" in data:
        import aws_sdk_databrew.types.threshold_unit

        out["unit"] = aws_sdk_databrew.types.threshold_unit.deserialize_json(
            data["Unit"]
        )
    return out
