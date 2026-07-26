"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_transform_input
    import capo_sagemaker.types.endpoint_input


class MonitoringInput(TypedDict, closed=True):
    endpoint_input: NotRequired["capo_sagemaker.types.endpoint_input.EndpointInput"]
    """<p>The endpoint for a monitoring job.</p>"""
    batch_transform_input: NotRequired[
        "capo_sagemaker.types.batch_transform_input.BatchTransformInput"
    ]
    """<p>Input object for the batch transform job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringInput) -> dict:
    out: dict = {}
    if "endpoint_input" in value:
        import capo_sagemaker.types.endpoint_input

        out["EndpointInput"] = (
            capo_sagemaker.types.endpoint_input.serialize_aws_json_1_1(
                value["endpoint_input"]
            )
        )
    if "batch_transform_input" in value:
        import capo_sagemaker.types.batch_transform_input

        out["BatchTransformInput"] = (
            capo_sagemaker.types.batch_transform_input.serialize_aws_json_1_1(
                value["batch_transform_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringInput:
    out: MonitoringInput = {}  # type: ignore[typeddict-item]
    if "EndpointInput" in data:
        import capo_sagemaker.types.endpoint_input

        out["endpoint_input"] = (
            capo_sagemaker.types.endpoint_input.deserialize_aws_json_1_1(
                data["EndpointInput"]
            )
        )
    if "BatchTransformInput" in data:
        import capo_sagemaker.types.batch_transform_input

        out["batch_transform_input"] = (
            capo_sagemaker.types.batch_transform_input.deserialize_aws_json_1_1(
                data["BatchTransformInput"]
            )
        )
    return out
