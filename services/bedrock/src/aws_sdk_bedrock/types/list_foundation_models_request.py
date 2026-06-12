"""Generated from Smithy shape ``com.amazonaws.bedrock#ListFoundationModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_type
    import aws_sdk_bedrock.types.model_customization
    import aws_sdk_bedrock.types.model_modality
    import aws_sdk_bedrock.types.provider


class ListFoundationModelsRequest(TypedDict):
    by_provider: NotRequired["aws_sdk_bedrock.types.provider.Provider"]
    """<p>Return models belonging to the model provider that you specify.</p>"""
    by_customization_type: NotRequired[
        "aws_sdk_bedrock.types.model_customization.ModelCustomization"
    ]
    """<p>Return models that support the customization type that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html\">Custom models</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>"""
    by_output_modality: NotRequired[
        "aws_sdk_bedrock.types.model_modality.ModelModality"
    ]
    """<p>Return models that support the output modality that you specify.</p>"""
    by_inference_type: NotRequired["aws_sdk_bedrock.types.inference_type.InferenceType"]
    """<p>Return models that support the inference type that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFoundationModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFoundationModelsRequest:
    out: ListFoundationModelsRequest = {}  # type: ignore[typeddict-item]
    return out
