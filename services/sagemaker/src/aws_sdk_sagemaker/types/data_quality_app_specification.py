"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataQualityAppSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.container_entrypoint
    import aws_sdk_sagemaker.types.image_uri
    import aws_sdk_sagemaker.types.monitoring_container_arguments
    import aws_sdk_sagemaker.types.monitoring_environment_map
    import aws_sdk_sagemaker.types.s3_uri


class DataQualityAppSpecification(TypedDict):
    image_uri: NotRequired["aws_sdk_sagemaker.types.image_uri.ImageUri"]
    """<p>The container image that the data quality monitoring job runs.</p>"""
    container_entrypoint: NotRequired[
        "aws_sdk_sagemaker.types.container_entrypoint.ContainerEntrypoint"
    ]
    """<p>The entrypoint for a container used to run a monitoring job.</p>"""
    container_arguments: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_container_arguments.MonitoringContainerArguments"
    ]
    """<p>The arguments to send to the container that the monitoring job runs.</p>"""
    record_preprocessor_source_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flattened JSON so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers.</p>"""
    post_analytics_processor_source_uri: NotRequired[
        "aws_sdk_sagemaker.types.s3_uri.S3Uri"
    ]
    """<p>An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_environment_map.MonitoringEnvironmentMap"
    ]
    """<p>Sets the environment variables in the container that the monitoring job runs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityAppSpecification) -> dict:
    out: dict = {}
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "container_entrypoint" in value:
        import aws_sdk_sagemaker.types.container_entrypoint

        out["ContainerEntrypoint"] = (
            aws_sdk_sagemaker.types.container_entrypoint.serialize_aws_json_1_1(
                value["container_entrypoint"]
            )
        )
    if "container_arguments" in value:
        import aws_sdk_sagemaker.types.monitoring_container_arguments

        out["ContainerArguments"] = (
            aws_sdk_sagemaker.types.monitoring_container_arguments.serialize_aws_json_1_1(
                value["container_arguments"]
            )
        )
    if "record_preprocessor_source_uri" in value:
        out["RecordPreprocessorSourceUri"] = value["record_preprocessor_source_uri"]
    if "post_analytics_processor_source_uri" in value:
        out["PostAnalyticsProcessorSourceUri"] = value[
            "post_analytics_processor_source_uri"
        ]
    if "environment" in value:
        import aws_sdk_sagemaker.types.monitoring_environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.monitoring_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityAppSpecification:
    out: DataQualityAppSpecification = {}  # type: ignore[typeddict-item]
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "ContainerEntrypoint" in data:
        import aws_sdk_sagemaker.types.container_entrypoint

        out["container_entrypoint"] = (
            aws_sdk_sagemaker.types.container_entrypoint.deserialize_aws_json_1_1(
                data["ContainerEntrypoint"]
            )
        )
    if "ContainerArguments" in data:
        import aws_sdk_sagemaker.types.monitoring_container_arguments

        out["container_arguments"] = (
            aws_sdk_sagemaker.types.monitoring_container_arguments.deserialize_aws_json_1_1(
                data["ContainerArguments"]
            )
        )
    if "RecordPreprocessorSourceUri" in data:
        out["record_preprocessor_source_uri"] = data["RecordPreprocessorSourceUri"]
    if "PostAnalyticsProcessorSourceUri" in data:
        out["post_analytics_processor_source_uri"] = data[
            "PostAnalyticsProcessorSourceUri"
        ]
    if "Environment" in data:
        import aws_sdk_sagemaker.types.monitoring_environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.monitoring_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
