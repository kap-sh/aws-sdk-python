"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateDataIntegrationFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.data_integration_flow_source_list
    import aws_sdk_supplychain.types.data_integration_flow_target
    import aws_sdk_supplychain.types.data_integration_flow_transformation
    import aws_sdk_supplychain.types.uuid


class UpdateDataIntegrationFlowRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The name of the DataIntegrationFlow to be updated.</p>"""
    sources: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
    ]
    """<p>The new source configurations for the DataIntegrationFlow.</p>"""
    transformation: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
    ]
    """<p>The new transformation configurations for the DataIntegrationFlow.</p>"""
    target: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
    ]
    """<p>The new target configurations for the DataIntegrationFlow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataIntegrationFlowRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import aws_sdk_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            aws_sdk_supplychain.types.data_integration_flow_source_list.serialize_json(
                value["sources"]
            )
        )
    if "transformation" in value:
        import aws_sdk_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            aws_sdk_supplychain.types.data_integration_flow_transformation.serialize_json(
                value["transformation"]
            )
        )
    if "target" in value:
        import aws_sdk_supplychain.types.data_integration_flow_target

        out["target"] = (
            aws_sdk_supplychain.types.data_integration_flow_target.serialize_json(
                value["target"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDataIntegrationFlowRequest:
    out: UpdateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import aws_sdk_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            aws_sdk_supplychain.types.data_integration_flow_source_list.deserialize_json(
                data["sources"]
            )
        )
    if "transformation" in data:
        import aws_sdk_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            aws_sdk_supplychain.types.data_integration_flow_transformation.deserialize_json(
                data["transformation"]
            )
        )
    if "target" in data:
        import aws_sdk_supplychain.types.data_integration_flow_target

        out["target"] = (
            aws_sdk_supplychain.types.data_integration_flow_target.deserialize_json(
                data["target"]
            )
        )
    return out
