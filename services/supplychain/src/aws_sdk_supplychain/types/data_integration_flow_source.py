"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_dataset_source_configuration
    import aws_sdk_supplychain.types.data_integration_flow_s3_source_configuration
    import aws_sdk_supplychain.types.data_integration_flow_source_name
    import aws_sdk_supplychain.types.data_integration_flow_source_type


class DataIntegrationFlowSource(TypedDict):
    source_type: "aws_sdk_supplychain.types.data_integration_flow_source_type.DataIntegrationFlowSourceType"
    """<p>The DataIntegrationFlow source type.</p>"""
    source_name: "aws_sdk_supplychain.types.data_integration_flow_source_name.DataIntegrationFlowSourceName"
    """<p>The DataIntegrationFlow source name that can be used as table alias in SQL transformation query.</p>"""
    s3_source: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_s3_source_configuration.DataIntegrationFlowS3SourceConfiguration"
    ]
    """<p>The S3 DataIntegrationFlow source.</p>"""
    dataset_source: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_dataset_source_configuration.DataIntegrationFlowDatasetSourceConfiguration"
    ]
    """<p>The dataset DataIntegrationFlow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowSource) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_source_type

    out["sourceType"] = (
        aws_sdk_supplychain.types.data_integration_flow_source_type.serialize_json(
            value["source_type"]
        )
    )
    out["sourceName"] = value["source_name"]
    if "s3_source" in value:
        import aws_sdk_supplychain.types.data_integration_flow_s3_source_configuration

        out["s3Source"] = (
            aws_sdk_supplychain.types.data_integration_flow_s3_source_configuration.serialize_json(
                value["s3_source"]
            )
        )
    if "dataset_source" in value:
        import aws_sdk_supplychain.types.data_integration_flow_dataset_source_configuration

        out["datasetSource"] = (
            aws_sdk_supplychain.types.data_integration_flow_dataset_source_configuration.serialize_json(
                value["dataset_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowSource:
    out: DataIntegrationFlowSource = {}  # type: ignore[typeddict-item]
    if "sourceType" in data:
        import aws_sdk_supplychain.types.data_integration_flow_source_type

        out["source_type"] = (
            aws_sdk_supplychain.types.data_integration_flow_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlowSource.source_type required")
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    else:
        raise DeserializationError("DataIntegrationFlowSource.source_name required")
    if "s3Source" in data:
        import aws_sdk_supplychain.types.data_integration_flow_s3_source_configuration

        out["s3_source"] = (
            aws_sdk_supplychain.types.data_integration_flow_s3_source_configuration.deserialize_json(
                data["s3Source"]
            )
        )
    if "datasetSource" in data:
        import aws_sdk_supplychain.types.data_integration_flow_dataset_source_configuration

        out["dataset_source"] = (
            aws_sdk_supplychain.types.data_integration_flow_dataset_source_configuration.deserialize_json(
                data["datasetSource"]
            )
        )
    return out
