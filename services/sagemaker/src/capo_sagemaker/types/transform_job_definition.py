"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJobDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_strategy
    import capo_sagemaker.types.max_concurrent_transforms
    import capo_sagemaker.types.max_payload_in_mb
    import capo_sagemaker.types.transform_environment_map
    import capo_sagemaker.types.transform_input
    import capo_sagemaker.types.transform_output
    import capo_sagemaker.types.transform_resources


class TransformJobDefinition(TypedDict, closed=True):
    max_concurrent_transforms: NotRequired[
        "capo_sagemaker.types.max_concurrent_transforms.MaxConcurrentTransforms"
    ]
    """<p>The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.</p>"""
    max_payload_in_mb: NotRequired[
        "capo_sagemaker.types.max_payload_in_mb.MaxPayloadInMB"
    ]
    """<p>The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).</p>"""
    batch_strategy: NotRequired["capo_sagemaker.types.batch_strategy.BatchStrategy"]
    """<p>A string that determines the number of records included in a single mini-batch.</p> <p> <code>SingleRecord</code> means only one record is used per mini-batch. <code>MultiRecord</code> means a mini-batch is set to contain as many records that can fit within the <code>MaxPayloadInMB</code> limit.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.transform_environment_map.TransformEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.</p>"""
    transform_input: NotRequired["capo_sagemaker.types.transform_input.TransformInput"]
    """<p>A description of the input source and the way the transform job consumes it.</p>"""
    transform_output: NotRequired[
        "capo_sagemaker.types.transform_output.TransformOutput"
    ]
    """<p>Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.</p>"""
    transform_resources: NotRequired[
        "capo_sagemaker.types.transform_resources.TransformResources"
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
        import capo_sagemaker.types.batch_strategy

        out["BatchStrategy"] = (
            capo_sagemaker.types.batch_strategy.serialize_aws_json_1_1(
                value["batch_strategy"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.transform_environment_map

        out["Environment"] = (
            capo_sagemaker.types.transform_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "transform_input" in value:
        import capo_sagemaker.types.transform_input

        out["TransformInput"] = (
            capo_sagemaker.types.transform_input.serialize_aws_json_1_1(
                value["transform_input"]
            )
        )
    if "transform_output" in value:
        import capo_sagemaker.types.transform_output

        out["TransformOutput"] = (
            capo_sagemaker.types.transform_output.serialize_aws_json_1_1(
                value["transform_output"]
            )
        )
    if "transform_resources" in value:
        import capo_sagemaker.types.transform_resources

        out["TransformResources"] = (
            capo_sagemaker.types.transform_resources.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.batch_strategy

        out["batch_strategy"] = (
            capo_sagemaker.types.batch_strategy.deserialize_aws_json_1_1(
                data["BatchStrategy"]
            )
        )
    if "Environment" in data:
        import capo_sagemaker.types.transform_environment_map

        out["environment"] = (
            capo_sagemaker.types.transform_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "TransformInput" in data:
        import capo_sagemaker.types.transform_input

        out["transform_input"] = (
            capo_sagemaker.types.transform_input.deserialize_aws_json_1_1(
                data["TransformInput"]
            )
        )
    if "TransformOutput" in data:
        import capo_sagemaker.types.transform_output

        out["transform_output"] = (
            capo_sagemaker.types.transform_output.deserialize_aws_json_1_1(
                data["TransformOutput"]
            )
        )
    if "TransformResources" in data:
        import capo_sagemaker.types.transform_resources

        out["transform_resources"] = (
            capo_sagemaker.types.transform_resources.deserialize_aws_json_1_1(
                data["TransformResources"]
            )
        )
    return out
