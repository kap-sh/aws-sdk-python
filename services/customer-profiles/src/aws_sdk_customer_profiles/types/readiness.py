"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Readiness``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.percentage_integer
    import aws_sdk_customer_profiles.types.text


class Readiness(TypedDict):
    progress_percentage: NotRequired[
        "aws_sdk_customer_profiles.types.percentage_integer.percentageInteger"
    ]
    """<p>Approximately how far the Calculated Attribute creation is from completion.</p>"""
    message: NotRequired["aws_sdk_customer_profiles.types.text.text"]
    """<p>Any customer messaging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Readiness) -> dict:
    out: dict = {}
    if "progress_percentage" in value:
        out["ProgressPercentage"] = value["progress_percentage"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> Readiness:
    out: Readiness = {}  # type: ignore[typeddict-item]
    if "ProgressPercentage" in data:
        out["progress_percentage"] = data["ProgressPercentage"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
