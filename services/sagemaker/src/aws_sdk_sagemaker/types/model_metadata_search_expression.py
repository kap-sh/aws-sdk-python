"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataSearchExpression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_metadata_filters


class ModelMetadataSearchExpression(TypedDict):
    filters: NotRequired[
        "aws_sdk_sagemaker.types.model_metadata_filters.ModelMetadataFilters"
    ]
    """<p>A list of filter objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetadataSearchExpression) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_sagemaker.types.model_metadata_filters

        out["Filters"] = (
            aws_sdk_sagemaker.types.model_metadata_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelMetadataSearchExpression:
    out: ModelMetadataSearchExpression = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_sagemaker.types.model_metadata_filters

        out["filters"] = (
            aws_sdk_sagemaker.types.model_metadata_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
