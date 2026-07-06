"""Generated from Smithy shape ``com.amazonaws.ecs#TotalLocalStorageGBRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_double


class TotalLocalStorageGBRequest(TypedDict, closed=True):
    min: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The minimum total local storage in GB. Instance types with less local storage are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The maximum total local storage in GB. Instance types with more local storage are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TotalLocalStorageGBRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TotalLocalStorageGBRequest:
    out: TotalLocalStorageGBRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    return out
