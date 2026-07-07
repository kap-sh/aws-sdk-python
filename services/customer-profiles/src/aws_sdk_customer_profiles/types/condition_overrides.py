"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ConditionOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.range_override


class ConditionOverrides(TypedDict, closed=True):
    range: NotRequired["aws_sdk_customer_profiles.types.range_override.RangeOverride"]
    """<p>The relative time period over which data is included in the aggregation for this override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionOverrides) -> dict:
    out: dict = {}
    if "range" in value:
        import aws_sdk_customer_profiles.types.range_override

        out["Range"] = aws_sdk_customer_profiles.types.range_override.serialize_json(
            value["range"]
        )
    return out


def deserialize_json(data: dict) -> ConditionOverrides:
    out: ConditionOverrides = {}  # type: ignore[typeddict-item]
    if "Range" in data:
        import aws_sdk_customer_profiles.types.range_override

        out["range"] = aws_sdk_customer_profiles.types.range_override.deserialize_json(
            data["Range"]
        )
    return out
