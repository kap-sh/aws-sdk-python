"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlow``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.data_integration_flow_source_list
    import aws_sdk_supplychain.types.data_integration_flow_target
    import aws_sdk_supplychain.types.data_integration_flow_transformation
    import aws_sdk_supplychain.types.uuid


class DataIntegrationFlow(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The DataIntegrationFlow instance ID.</p>"""
    name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The DataIntegrationFlow name.</p>"""
    sources: "aws_sdk_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
    """<p>The DataIntegrationFlow source configurations.</p>"""
    transformation: "aws_sdk_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
    """<p>The DataIntegrationFlow transformation configurations.</p>"""
    target: "aws_sdk_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
    """<p>The DataIntegrationFlow target configuration.</p>"""
    created_time: "datetime.datetime"
    """<p>The DataIntegrationFlow creation timestamp.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The DataIntegrationFlow last modified timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlow) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["name"] = value["name"]
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
    import aws_sdk_supplychain.types._prelude.timestamp

    out["createdTime"] = aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_supplychain.types._prelude.timestamp

    out["lastModifiedTime"] = (
        aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlow:
    out: DataIntegrationFlow = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("DataIntegrationFlow.instance_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataIntegrationFlow.name required")
    if "sources" in data:
        import aws_sdk_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            aws_sdk_supplychain.types.data_integration_flow_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.sources required")
    if "transformation" in data:
        import aws_sdk_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            aws_sdk_supplychain.types.data_integration_flow_transformation.deserialize_json(
                data["transformation"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.transformation required")
    if "target" in data:
        import aws_sdk_supplychain.types.data_integration_flow_target

        out["target"] = (
            aws_sdk_supplychain.types.data_integration_flow_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.target required")
    if "createdTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.created_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.last_modified_time required")
    return out
