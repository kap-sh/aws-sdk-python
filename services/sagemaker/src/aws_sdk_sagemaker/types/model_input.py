"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.data_input_config


class ModelInput(TypedDict, closed=True):
    data_input_config: NotRequired[
        "aws_sdk_sagemaker.types.data_input_config.DataInputConfig"
    ]
    """<p>The input configuration object for the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelInput) -> dict:
    out: dict = {}
    if "data_input_config" in value:
        out["DataInputConfig"] = value["data_input_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelInput:
    out: ModelInput = {}  # type: ignore[typeddict-item]
    if "DataInputConfig" in data:
        out["data_input_config"] = data["DataInputConfig"]
    return out
