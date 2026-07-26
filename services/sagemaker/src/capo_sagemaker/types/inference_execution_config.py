"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExecutionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_execution_mode


class InferenceExecutionConfig(TypedDict, closed=True):
    mode: NotRequired[
        "capo_sagemaker.types.inference_execution_mode.InferenceExecutionMode"
    ]
    """<p>How containers in a multi-container are run. The following values are valid.</p> <ul> <li> <p> <code>SERIAL</code> - Containers run as a serial pipeline.</p> </li> <li> <p> <code>DIRECT</code> - Only the individual container that you specify is run.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExecutionConfig) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_sagemaker.types.inference_execution_mode

        out["Mode"] = (
            capo_sagemaker.types.inference_execution_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceExecutionConfig:
    out: InferenceExecutionConfig = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import capo_sagemaker.types.inference_execution_mode

        out["mode"] = (
            capo_sagemaker.types.inference_execution_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    return out
