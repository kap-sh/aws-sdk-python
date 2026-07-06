"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.configurations
    import aws_sdk_datazone.types.connection_id
    import aws_sdk_datazone.types.connection_name
    import aws_sdk_datazone.types.connection_properties_output
    import aws_sdk_datazone.types.connection_scope
    import aws_sdk_datazone.types.connection_type
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.physical_endpoints
    import aws_sdk_datazone.types.project_id


class UpdateConnectionOutput(TypedDict, closed=True):
    configurations: NotRequired["aws_sdk_datazone.types.configurations.Configurations"]
    """<p>The configurations of the connection.</p>"""
    connection_id: "aws_sdk_datazone.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The connection description.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where a connection is to be updated.</p>"""
    domain_unit_id: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit where a connection is to be updated.</p>"""
    environment_id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment where a connection is to be updated.</p>"""
    name: "aws_sdk_datazone.types.connection_name.ConnectionName"
    """<p>The name of the connection.</p>"""
    physical_endpoints: "aws_sdk_datazone.types.physical_endpoints.PhysicalEndpoints"
    """<p>The physical endpoints of the connection.</p>"""
    project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The project ID of the connection.</p>"""
    props: NotRequired[
        "aws_sdk_datazone.types.connection_properties_output.ConnectionPropertiesOutput"
    ]
    """<p>The connection props.</p>"""
    type: "aws_sdk_datazone.types.connection_type.ConnectionType"
    """<p>The connection type.</p>"""
    scope: NotRequired["aws_sdk_datazone.types.connection_scope.ConnectionScope"]
    """<p>The scope of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectionOutput) -> dict:
    out: dict = {}
    if "configurations" in value:
        import aws_sdk_datazone.types.configurations

        out["configurations"] = aws_sdk_datazone.types.configurations.serialize_json(
            value["configurations"]
        )
    out["connectionId"] = value["connection_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["domainId"] = value["domain_id"]
    out["domainUnitId"] = value["domain_unit_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    out["name"] = value["name"]
    import aws_sdk_datazone.types.physical_endpoints

    out["physicalEndpoints"] = aws_sdk_datazone.types.physical_endpoints.serialize_json(
        value["physical_endpoints"]
    )
    if "project_id" in value:
        out["projectId"] = value["project_id"]
    if "props" in value:
        import aws_sdk_datazone.types.connection_properties_output

        out["props"] = (
            aws_sdk_datazone.types.connection_properties_output.serialize_json(
                value["props"]
            )
        )
    import aws_sdk_datazone.types.connection_type

    out["type"] = aws_sdk_datazone.types.connection_type.serialize_json(value["type"])
    if "scope" in value:
        import aws_sdk_datazone.types.connection_scope

        out["scope"] = aws_sdk_datazone.types.connection_scope.serialize_json(
            value["scope"]
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectionOutput:
    out: UpdateConnectionOutput = {}  # type: ignore[typeddict-item]
    if "configurations" in data:
        import aws_sdk_datazone.types.configurations

        out["configurations"] = aws_sdk_datazone.types.configurations.deserialize_json(
            data["configurations"]
        )
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError("UpdateConnectionOutput.connection_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateConnectionOutput.domain_id required")
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    else:
        raise DeserializationError("UpdateConnectionOutput.domain_unit_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateConnectionOutput.name required")
    if "physicalEndpoints" in data:
        import aws_sdk_datazone.types.physical_endpoints

        out["physical_endpoints"] = (
            aws_sdk_datazone.types.physical_endpoints.deserialize_json(
                data["physicalEndpoints"]
            )
        )
    else:
        raise DeserializationError("UpdateConnectionOutput.physical_endpoints required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    if "props" in data:
        import aws_sdk_datazone.types.connection_properties_output

        out["props"] = (
            aws_sdk_datazone.types.connection_properties_output.deserialize_json(
                data["props"]
            )
        )
    if "type" in data:
        import aws_sdk_datazone.types.connection_type

        out["type"] = aws_sdk_datazone.types.connection_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("UpdateConnectionOutput.type required")
    if "scope" in data:
        import aws_sdk_datazone.types.connection_scope

        out["scope"] = aws_sdk_datazone.types.connection_scope.deserialize_json(
            data["scope"]
        )
    return out
