"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_metadata_filter_type
    import aws_sdk_sagemaker.types.string256


class ModelMetadataFilter(TypedDict):
    name: NotRequired[
        "aws_sdk_sagemaker.types.model_metadata_filter_type.ModelMetadataFilterType"
    ]
    """<p>The name of the of the model to filter by.</p>"""
    value: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The value to filter the model metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetadataFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_sagemaker.types.model_metadata_filter_type

        out["Name"] = (
            aws_sdk_sagemaker.types.model_metadata_filter_type.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelMetadataFilter:
    out: ModelMetadataFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_sagemaker.types.model_metadata_filter_type

        out["name"] = (
            aws_sdk_sagemaker.types.model_metadata_filter_type.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
