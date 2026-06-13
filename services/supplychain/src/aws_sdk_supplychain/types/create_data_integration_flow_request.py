"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateDataIntegrationFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.data_integration_flow_source_list
    import aws_sdk_supplychain.types.data_integration_flow_target
    import aws_sdk_supplychain.types.data_integration_flow_transformation
    import aws_sdk_supplychain.types.tag_map
    import aws_sdk_supplychain.types.uuid


class CreateDataIntegrationFlowRequest(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>Name of the DataIntegrationFlow.</p>"""
    sources: "aws_sdk_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
    """<p>The source configurations for DataIntegrationFlow.</p>"""
    transformation: "aws_sdk_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
    """<p>The transformation configurations for DataIntegrationFlow.</p>"""
    target: "aws_sdk_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
    """<p>The target configurations for DataIntegrationFlow.</p>"""
    tags: NotRequired["aws_sdk_supplychain.types.tag_map.TagMap"]
    """<p>The tags of the DataIntegrationFlow to be created</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataIntegrationFlowRequest) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_source_list

    out["sources"] = (
        aws_sdk_supplychain.types.data_integration_flow_source_list.serialize_json(
            value["sources"]
        )
    )
    import aws_sdk_supplychain.types.data_integration_flow_transformation

    out["transformation"] = (
        aws_sdk_supplychain.types.data_integration_flow_transformation.serialize_json(
            value["transformation"]
        )
    )
    import aws_sdk_supplychain.types.data_integration_flow_target

    out["target"] = (
        aws_sdk_supplychain.types.data_integration_flow_target.serialize_json(
            value["target"]
        )
    )
    if "tags" in value:
        import aws_sdk_supplychain.types.tag_map

        out["tags"] = aws_sdk_supplychain.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataIntegrationFlowRequest:
    out: CreateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import aws_sdk_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            aws_sdk_supplychain.types.data_integration_flow_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("CreateDataIntegrationFlowRequest.sources required")
    if "transformation" in data:
        import aws_sdk_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            aws_sdk_supplychain.types.data_integration_flow_transformation.deserialize_json(
                data["transformation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataIntegrationFlowRequest.transformation required"
        )
    if "target" in data:
        import aws_sdk_supplychain.types.data_integration_flow_target

        out["target"] = (
            aws_sdk_supplychain.types.data_integration_flow_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError("CreateDataIntegrationFlowRequest.target required")
    if "tags" in data:
        import aws_sdk_supplychain.types.tag_map

        out["tags"] = aws_sdk_supplychain.types.tag_map.deserialize_json(data["tags"])
    return out
