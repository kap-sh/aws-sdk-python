"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalModelSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.model_source
    import aws_sdk_frauddetector.types.string


class ExternalModelSummary(TypedDict):
    model_endpoint: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The endpoint of the Amazon SageMaker model.</p>"""
    model_source: NotRequired["aws_sdk_frauddetector.types.model_source.ModelSource"]
    """<p>The source of the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalModelSummary) -> dict:
    out: dict = {}
    if "model_endpoint" in value:
        out["modelEndpoint"] = value["model_endpoint"]
    if "model_source" in value:
        import aws_sdk_frauddetector.types.model_source

        out["modelSource"] = (
            aws_sdk_frauddetector.types.model_source.serialize_aws_json_1_1(
                value["model_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalModelSummary:
    out: ExternalModelSummary = {}  # type: ignore[typeddict-item]
    if "modelEndpoint" in data:
        out["model_endpoint"] = data["modelEndpoint"]
    if "modelSource" in data:
        import aws_sdk_frauddetector.types.model_source

        out["model_source"] = (
            aws_sdk_frauddetector.types.model_source.deserialize_aws_json_1_1(
                data["modelSource"]
            )
        )
    return out
