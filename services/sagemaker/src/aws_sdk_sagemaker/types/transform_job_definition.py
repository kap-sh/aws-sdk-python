"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJobDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_strategy
    import aws_sdk_sagemaker.types.max_concurrent_transforms
    import aws_sdk_sagemaker.types.max_payload_in_mb
    import aws_sdk_sagemaker.types.transform_environment_map
    import aws_sdk_sagemaker.types.transform_input
    import aws_sdk_sagemaker.types.transform_output
    import aws_sdk_sagemaker.types.transform_resources


class TransformJobDefinition(TypedDict):
    max_concurrent_transforms: NotRequired[
        "aws_sdk_sagemaker.types.max_concurrent_transforms.MaxConcurrentTransforms"
    ]
    """<p>The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.</p>"""
    max_payload_in_mb: NotRequired[
        "aws_sdk_sagemaker.types.max_payload_in_mb.MaxPayloadInMB"
    ]
    """<p>The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).</p>"""
    batch_strategy: NotRequired["aws_sdk_sagemaker.types.batch_strategy.BatchStrategy"]
    """<p>A string that determines the number of records included in a single mini-batch.</p> <p> <code>SingleRecord</code> means only one record is used per mini-batch. <code>MultiRecord</code> means a mini-batch is set to contain as many records that can fit within the <code>MaxPayloadInMB</code> limit.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.transform_environment_map.TransformEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.</p>"""
    transform_input: NotRequired[
        "aws_sdk_sagemaker.types.transform_input.TransformInput"
    ]
    """<p>A description of the input source and the way the transform job consumes it.</p>"""
    transform_output: NotRequired[
        "aws_sdk_sagemaker.types.transform_output.TransformOutput"
    ]
    """<p>Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.</p>"""
    transform_resources: NotRequired[
        "aws_sdk_sagemaker.types.transform_resources.TransformResources"
    ]
    """<p>Identifies the ML compute instances for the transform job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformJobDefinition) -> dict:
    out: dict = {}
    if "max_concurrent_transforms" in value:
        out["MaxConcurrentTransforms"] = value["max_concurrent_transforms"]
    if "max_payload_in_mb" in value:
        out["MaxPayloadInMB"] = value["max_payload_in_mb"]
    if "batch_strategy" in value:
        import aws_sdk_sagemaker.types.batch_strategy

        out["BatchStrategy"] = (
            aws_sdk_sagemaker.types.batch_strategy.serialize_aws_json_1_1(
                value["batch_strategy"]
            )
        )
    if "environment" in value:
        import aws_sdk_sagemaker.types.transform_environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.transform_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "transform_input" in value:
        import aws_sdk_sagemaker.types.transform_input

        out["TransformInput"] = (
            aws_sdk_sagemaker.types.transform_input.serialize_aws_json_1_1(
                value["transform_input"]
            )
        )
    if "transform_output" in value:
        import aws_sdk_sagemaker.types.transform_output

        out["TransformOutput"] = (
            aws_sdk_sagemaker.types.transform_output.serialize_aws_json_1_1(
                value["transform_output"]
            )
        )
    if "transform_resources" in value:
        import aws_sdk_sagemaker.types.transform_resources

        out["TransformResources"] = (
            aws_sdk_sagemaker.types.transform_resources.serialize_aws_json_1_1(
                value["transform_resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformJobDefinition:
    out: TransformJobDefinition = {}  # type: ignore[typeddict-item]
    if "MaxConcurrentTransforms" in data:
        out["max_concurrent_transforms"] = data["MaxConcurrentTransforms"]
    if "MaxPayloadInMB" in data:
        out["max_payload_in_mb"] = data["MaxPayloadInMB"]
    if "BatchStrategy" in data:
        import aws_sdk_sagemaker.types.batch_strategy

        out["batch_strategy"] = (
            aws_sdk_sagemaker.types.batch_strategy.deserialize_aws_json_1_1(
                data["BatchStrategy"]
            )
        )
    if "Environment" in data:
        import aws_sdk_sagemaker.types.transform_environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.transform_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "TransformInput" in data:
        import aws_sdk_sagemaker.types.transform_input

        out["transform_input"] = (
            aws_sdk_sagemaker.types.transform_input.deserialize_aws_json_1_1(
                data["TransformInput"]
            )
        )
    if "TransformOutput" in data:
        import aws_sdk_sagemaker.types.transform_output

        out["transform_output"] = (
            aws_sdk_sagemaker.types.transform_output.deserialize_aws_json_1_1(
                data["TransformOutput"]
            )
        )
    if "TransformResources" in data:
        import aws_sdk_sagemaker.types.transform_resources

        out["transform_resources"] = (
            aws_sdk_sagemaker.types.transform_resources.deserialize_aws_json_1_1(
                data["TransformResources"]
            )
        )
    return out
