"""Generated from Smithy shape ``com.amazonaws.forecast#Featurization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.featurization_pipeline
    import aws_sdk_forecast.types.name


class Featurization(TypedDict):
    attribute_name: "aws_sdk_forecast.types.name.Name"
    """<p>The name of the schema attribute that specifies the data field to be featurized. Amazon Forecast supports the target field of the <code>TARGET_TIME_SERIES</code> and the <code>RELATED_TIME_SERIES</code> datasets. For example, for the <code>RETAIL</code> domain, the target is <code>demand</code>, and for the <code>CUSTOM</code> domain, the target is <code>target_value</code>. For more information, see <a>howitworks-missing-values</a>.</p>"""
    featurization_pipeline: NotRequired[
        "aws_sdk_forecast.types.featurization_pipeline.FeaturizationPipeline"
    ]
    """<p>An array of one <code>FeaturizationMethod</code> object that specifies the feature transformation method.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Featurization) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    if "featurization_pipeline" in value:
        import aws_sdk_forecast.types.featurization_pipeline

        out["FeaturizationPipeline"] = (
            aws_sdk_forecast.types.featurization_pipeline.serialize_aws_json_1_1(
                value["featurization_pipeline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Featurization:
    out: Featurization = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("Featurization.attribute_name required")
    if "FeaturizationPipeline" in data:
        import aws_sdk_forecast.types.featurization_pipeline

        out["featurization_pipeline"] = (
            aws_sdk_forecast.types.featurization_pipeline.deserialize_aws_json_1_1(
                data["FeaturizationPipeline"]
            )
        )
    return out
