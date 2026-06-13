"""Generated from Smithy shape ``com.amazonaws.emr#ModifyClusterInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.string


class ModifyClusterInput(TypedDict):
    cluster_id: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The unique identifier of the cluster.</p>"""
    step_concurrency_level: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The number of steps that can be executed concurrently. You can specify a minimum of 1 step and a maximum of 256 steps. We recommend that you do not change this parameter while steps are running or the <code>ActionOnFailure</code> setting may not behave as expected. For more information see <a>Step$ActionOnFailure</a>.</p>"""
    extended_support: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClusterInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "step_concurrency_level" in value:
        out["StepConcurrencyLevel"] = value["step_concurrency_level"]
    if "extended_support" in value:
        out["ExtendedSupport"] = value["extended_support"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClusterInput:
    out: ModifyClusterInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "StepConcurrencyLevel" in data:
        out["step_concurrency_level"] = data["StepConcurrencyLevel"]
    if "ExtendedSupport" in data:
        out["extended_support"] = data["ExtendedSupport"]
    return out
