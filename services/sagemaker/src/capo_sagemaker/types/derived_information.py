"""Generated from Smithy shape ``com.amazonaws.sagemaker#DerivedInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.data_input_config


class DerivedInformation(TypedDict, closed=True):
    derived_data_input_config: NotRequired[
        "capo_sagemaker.types.data_input_config.DataInputConfig"
    ]
    """<p>The data input configuration that SageMaker Neo automatically derived for the model. When SageMaker Neo derives this information, you don't need to specify the data input configuration when you create a compilation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DerivedInformation) -> dict:
    out: dict = {}
    if "derived_data_input_config" in value:
        out["DerivedDataInputConfig"] = value["derived_data_input_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DerivedInformation:
    out: DerivedInformation = {}  # type: ignore[typeddict-item]
    if "DerivedDataInputConfig" in data:
        out["derived_data_input_config"] = data["DerivedDataInputConfig"]
    return out
