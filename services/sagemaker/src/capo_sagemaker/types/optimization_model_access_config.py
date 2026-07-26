"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationModelAccessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.optimization_model_accept_eula


class OptimizationModelAccessConfig(TypedDict, closed=True):
    accept_eula: NotRequired[
        "capo_sagemaker.types.optimization_model_accept_eula.OptimizationModelAcceptEula"
    ]
    """<p>Specifies agreement to the model end-user license agreement (EULA). The <code>AcceptEula</code> value must be explicitly defined as <code>True</code> in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationModelAccessConfig) -> dict:
    out: dict = {}
    if "accept_eula" in value:
        out["AcceptEula"] = value["accept_eula"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationModelAccessConfig:
    out: OptimizationModelAccessConfig = {}  # type: ignore[typeddict-item]
    if "AcceptEula" in data:
        out["accept_eula"] = data["AcceptEula"]
    return out
