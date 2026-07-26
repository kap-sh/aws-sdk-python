"""Generated from Smithy shape ``com.amazonaws.detective#Indicator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.indicator_detail
    import capo_detective.types.indicator_type


class Indicator(TypedDict, closed=True):
    indicator_type: NotRequired["capo_detective.types.indicator_type.IndicatorType"]
    """<p>The type of indicator. </p>"""
    indicator_detail: NotRequired[
        "capo_detective.types.indicator_detail.IndicatorDetail"
    ]
    """<p>Details about the indicators of compromise that are used to determine if a resource is involved in a security incident. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Indicator) -> dict:
    out: dict = {}
    if "indicator_type" in value:
        import capo_detective.types.indicator_type

        out["IndicatorType"] = capo_detective.types.indicator_type.serialize_json(
            value["indicator_type"]
        )
    if "indicator_detail" in value:
        import capo_detective.types.indicator_detail

        out["IndicatorDetail"] = capo_detective.types.indicator_detail.serialize_json(
            value["indicator_detail"]
        )
    return out


def deserialize_json(data: dict) -> Indicator:
    out: Indicator = {}  # type: ignore[typeddict-item]
    if "IndicatorType" in data:
        import capo_detective.types.indicator_type

        out["indicator_type"] = capo_detective.types.indicator_type.deserialize_json(
            data["IndicatorType"]
        )
    if "IndicatorDetail" in data:
        import capo_detective.types.indicator_detail

        out["indicator_detail"] = (
            capo_detective.types.indicator_detail.deserialize_json(
                data["IndicatorDetail"]
            )
        )
    return out
