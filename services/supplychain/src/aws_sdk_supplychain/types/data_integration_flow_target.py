"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_dataset_target_configuration
    import aws_sdk_supplychain.types.data_integration_flow_s3_target_configuration
    import aws_sdk_supplychain.types.data_integration_flow_target_type


class DataIntegrationFlowTarget(TypedDict, closed=True):
    target_type: "aws_sdk_supplychain.types.data_integration_flow_target_type.DataIntegrationFlowTargetType"
    """<p>The DataIntegrationFlow target type.</p>"""
    s3_target: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_s3_target_configuration.DataIntegrationFlowS3TargetConfiguration"
    ]
    """<p>The S3 DataIntegrationFlow target.</p>"""
    dataset_target: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_dataset_target_configuration.DataIntegrationFlowDatasetTargetConfiguration"
    ]
    """<p>The dataset DataIntegrationFlow target. Note that for AWS Supply Chain dataset under <b>asc</b> namespace, it has a connection_id internal field that is not allowed to be provided by client directly, they will be auto populated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowTarget) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_target_type

    out["targetType"] = (
        aws_sdk_supplychain.types.data_integration_flow_target_type.serialize_json(
            value["target_type"]
        )
    )
    if "s3_target" in value:
        import aws_sdk_supplychain.types.data_integration_flow_s3_target_configuration

        out["s3Target"] = (
            aws_sdk_supplychain.types.data_integration_flow_s3_target_configuration.serialize_json(
                value["s3_target"]
            )
        )
    if "dataset_target" in value:
        import aws_sdk_supplychain.types.data_integration_flow_dataset_target_configuration

        out["datasetTarget"] = (
            aws_sdk_supplychain.types.data_integration_flow_dataset_target_configuration.serialize_json(
                value["dataset_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowTarget:
    out: DataIntegrationFlowTarget = {}  # type: ignore[typeddict-item]
    if "targetType" in data:
        import aws_sdk_supplychain.types.data_integration_flow_target_type

        out["target_type"] = (
            aws_sdk_supplychain.types.data_integration_flow_target_type.deserialize_json(
                data["targetType"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlowTarget.target_type required")
    if "s3Target" in data:
        import aws_sdk_supplychain.types.data_integration_flow_s3_target_configuration

        out["s3_target"] = (
            aws_sdk_supplychain.types.data_integration_flow_s3_target_configuration.deserialize_json(
                data["s3Target"]
            )
        )
    if "datasetTarget" in data:
        import aws_sdk_supplychain.types.data_integration_flow_dataset_target_configuration

        out["dataset_target"] = (
            aws_sdk_supplychain.types.data_integration_flow_dataset_target_configuration.deserialize_json(
                data["datasetTarget"]
            )
        )
    return out
