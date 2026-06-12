"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelBiasAppSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_uri
    import aws_sdk_sagemaker.types.monitoring_environment_map
    import aws_sdk_sagemaker.types.s3_uri


class ModelBiasAppSpecification(TypedDict):
    image_uri: NotRequired["aws_sdk_sagemaker.types.image_uri.ImageUri"]
    """<p>The container image to be run by the model bias job.</p>"""
    config_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>JSON formatted S3 file that defines bias parameters. For more information on this JSON configuration file, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-bias-parameters.html\">Configure bias parameters</a>.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_environment_map.MonitoringEnvironmentMap"
    ]
    """<p>Sets the environment variables in the Docker container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelBiasAppSpecification) -> dict:
    out: dict = {}
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "config_uri" in value:
        out["ConfigUri"] = value["config_uri"]
    if "environment" in value:
        import aws_sdk_sagemaker.types.monitoring_environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.monitoring_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelBiasAppSpecification:
    out: ModelBiasAppSpecification = {}  # type: ignore[typeddict-item]
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "ConfigUri" in data:
        out["config_uri"] = data["ConfigUri"]
    if "Environment" in data:
        import aws_sdk_sagemaker.types.monitoring_environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.monitoring_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
