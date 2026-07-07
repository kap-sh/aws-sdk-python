"""Generated from Smithy shape ``com.amazonaws.emr#ScalingConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.integer


class ScalingConstraints(TypedDict, closed=True):
    min_capacity: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.</p>"""
    max_capacity: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingConstraints) -> dict:
    out: dict = {}
    if "min_capacity" in value:
        out["MinCapacity"] = value["min_capacity"]
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingConstraints:
    out: ScalingConstraints = {}  # type: ignore[typeddict-item]
    if "MinCapacity" in data:
        out["min_capacity"] = data["MinCapacity"]
    if "MaxCapacity" in data:
        out["max_capacity"] = data["MaxCapacity"]
    return out
