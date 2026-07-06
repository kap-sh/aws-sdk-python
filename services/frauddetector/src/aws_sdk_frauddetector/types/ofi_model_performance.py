"""Generated from Smithy shape ``com.amazonaws.frauddetector#OFIModelPerformance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float
    import aws_sdk_frauddetector.types.uncertainty_range


class OFIModelPerformance(TypedDict, closed=True):
    auc: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The area under the curve (auc). This summarizes the total positive rate (tpr) and false positive rate (FPR) across all possible model score thresholds. </p>"""
    uncertainty_range: NotRequired[
        "aws_sdk_frauddetector.types.uncertainty_range.UncertaintyRange"
    ]
    """<p> Indicates the range of area under curve (auc) expected from the OFI model. A range greater than 0.1 indicates higher model uncertainity. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OFIModelPerformance) -> dict:
    out: dict = {}
    if "auc" in value:
        out["auc"] = value["auc"]
    if "uncertainty_range" in value:
        import aws_sdk_frauddetector.types.uncertainty_range

        out["uncertaintyRange"] = (
            aws_sdk_frauddetector.types.uncertainty_range.serialize_aws_json_1_1(
                value["uncertainty_range"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OFIModelPerformance:
    out: OFIModelPerformance = {}  # type: ignore[typeddict-item]
    if "auc" in data:
        out["auc"] = data["auc"]
    if "uncertaintyRange" in data:
        import aws_sdk_frauddetector.types.uncertainty_range

        out["uncertainty_range"] = (
            aws_sdk_frauddetector.types.uncertainty_range.deserialize_aws_json_1_1(
                data["uncertaintyRange"]
            )
        )
    return out
