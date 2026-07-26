"""Generated from Smithy shape ``com.amazonaws.frauddetector#UncertaintyRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.float


class UncertaintyRange(TypedDict, closed=True):
    lower_bound_value: "capo_frauddetector.types.float.float"
    """<p> The lower bound value of the area under curve (auc). </p>"""
    upper_bound_value: "capo_frauddetector.types.float.float"
    """<p> The upper bound value of the area under curve (auc). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UncertaintyRange) -> dict:
    out: dict = {}
    out["lowerBoundValue"] = value["lower_bound_value"]
    out["upperBoundValue"] = value["upper_bound_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UncertaintyRange:
    out: UncertaintyRange = {}  # type: ignore[typeddict-item]
    if "lowerBoundValue" in data:
        out["lower_bound_value"] = data["lowerBoundValue"]
    else:
        raise DeserializationError("UncertaintyRange.lower_bound_value required")
    if "upperBoundValue" in data:
        out["upper_bound_value"] = data["upperBoundValue"]
    else:
        raise DeserializationError("UncertaintyRange.upper_bound_value required")
    return out
