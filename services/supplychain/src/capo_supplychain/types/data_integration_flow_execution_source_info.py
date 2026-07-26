"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowExecutionSourceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_dataset_source
    import capo_supplychain.types.data_integration_flow_s3_source
    import capo_supplychain.types.data_integration_flow_source_type


class DataIntegrationFlowExecutionSourceInfo(TypedDict, closed=True):
    source_type: "capo_supplychain.types.data_integration_flow_source_type.DataIntegrationFlowSourceType"
    """<p>The data integration flow execution source type.</p>"""
    s3_source: NotRequired[
        "capo_supplychain.types.data_integration_flow_s3_source.DataIntegrationFlowS3Source"
    ]
    """<p>The source details of a flow execution with S3 source.</p>"""
    dataset_source: NotRequired[
        "capo_supplychain.types.data_integration_flow_dataset_source.DataIntegrationFlowDatasetSource"
    ]
    """<p>The source details of a flow execution with dataset source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowExecutionSourceInfo) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_source_type

    out["sourceType"] = (
        capo_supplychain.types.data_integration_flow_source_type.serialize_json(
            value["source_type"]
        )
    )
    if "s3_source" in value:
        import capo_supplychain.types.data_integration_flow_s3_source

        out["s3Source"] = (
            capo_supplychain.types.data_integration_flow_s3_source.serialize_json(
                value["s3_source"]
            )
        )
    if "dataset_source" in value:
        import capo_supplychain.types.data_integration_flow_dataset_source

        out["datasetSource"] = (
            capo_supplychain.types.data_integration_flow_dataset_source.serialize_json(
                value["dataset_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowExecutionSourceInfo:
    out: DataIntegrationFlowExecutionSourceInfo = {}  # type: ignore[typeddict-item]
    if "sourceType" in data:
        import capo_supplychain.types.data_integration_flow_source_type

        out["source_type"] = (
            capo_supplychain.types.data_integration_flow_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationFlowExecutionSourceInfo.source_type required"
        )
    if "s3Source" in data:
        import capo_supplychain.types.data_integration_flow_s3_source

        out["s3_source"] = (
            capo_supplychain.types.data_integration_flow_s3_source.deserialize_json(
                data["s3Source"]
            )
        )
    if "datasetSource" in data:
        import capo_supplychain.types.data_integration_flow_dataset_source

        out["dataset_source"] = (
            capo_supplychain.types.data_integration_flow_dataset_source.deserialize_json(
                data["datasetSource"]
            )
        )
    return out
