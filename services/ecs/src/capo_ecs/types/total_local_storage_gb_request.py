"""Generated from Smithy shape ``com.amazonaws.ecs#TotalLocalStorageGBRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_double


class TotalLocalStorageGBRequest(TypedDict, closed=True):
    min: NotRequired["capo_ecs.types.boxed_double.BoxedDouble"]
    """<p>The minimum total local storage in GB. Instance types with less local storage are excluded from selection.</p>"""
    max: NotRequired["capo_ecs.types.boxed_double.BoxedDouble"]
    """<p>The maximum total local storage in GB. Instance types with more local storage are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TotalLocalStorageGBRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "max" in value:
        out["max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TotalLocalStorageGBRequest:
    out: TotalLocalStorageGBRequest = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = float(data["min"])
    if data.get("max") is not None:
        out["max"] = float(data["max"])
    return out
