"""Generated from Smithy shape ``com.amazonaws.frauddetector#ATIModelPerformance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float


class ATIModelPerformance(TypedDict, closed=True):
    asi: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The anomaly separation index (ASI) score. This metric summarizes the overall ability of the model to separate anomalous activities from the normal behavior. Depending on the business, a large fraction of these anomalous activities can be malicious and correspond to the account takeover attacks. A model with no separability power will have the lowest possible ASI score of 0.5, whereas the a model with a high separability power will have the highest possible ASI score of 1.0 </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ATIModelPerformance) -> dict:
    out: dict = {}
    if "asi" in value:
        out["asi"] = value["asi"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ATIModelPerformance:
    out: ATIModelPerformance = {}  # type: ignore[typeddict-item]
    if "asi" in data:
        out["asi"] = data["asi"]
    return out
