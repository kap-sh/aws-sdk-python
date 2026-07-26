"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingFeatureStoreOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_group_name


class ProcessingFeatureStoreOutput(TypedDict, closed=True):
    feature_group_name: NotRequired[
        "capo_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>The name of the Amazon SageMaker FeatureGroup to use as the destination for processing job output. Note that your processing script is responsible for putting records into your Feature Store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingFeatureStoreOutput) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingFeatureStoreOutput:
    out: ProcessingFeatureStoreOutput = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    return out
