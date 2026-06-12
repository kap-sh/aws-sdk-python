"""Generated from Smithy shape ``com.amazonaws.emr#ModifyClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.integer


class ModifyClusterOutput(TypedDict):
    step_concurrency_level: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The number of steps that can be executed concurrently.</p>"""
    extended_support: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClusterOutput) -> dict:
    out: dict = {}
    if "step_concurrency_level" in value:
        out["StepConcurrencyLevel"] = value["step_concurrency_level"]
    if "extended_support" in value:
        out["ExtendedSupport"] = value["extended_support"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClusterOutput:
    out: ModifyClusterOutput = {}  # type: ignore[typeddict-item]
    if "StepConcurrencyLevel" in data:
        out["step_concurrency_level"] = data["StepConcurrencyLevel"]
    if "ExtendedSupport" in data:
        out["extended_support"] = data["ExtendedSupport"]
    return out
