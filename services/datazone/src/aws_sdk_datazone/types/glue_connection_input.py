"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.authentication_configuration_input
    import aws_sdk_datazone.types.compute_environments_list
    import aws_sdk_datazone.types.connection_properties
    import aws_sdk_datazone.types.glue_connection_type
    import aws_sdk_datazone.types.physical_connection_requirements
    import aws_sdk_datazone.types.property_map


class GlueConnectionInput(TypedDict):
    connection_properties: NotRequired[
        "aws_sdk_datazone.types.connection_properties.ConnectionProperties"
    ]
    """<p>The connection properties of the Amazon Web Services Glue connection.</p>"""
    physical_connection_requirements: NotRequired[
        "aws_sdk_datazone.types.physical_connection_requirements.PhysicalConnectionRequirements"
    ]
    """<p>The physical connection requirements for the Amazon Web Services Glue connection.</p>"""
    name: NotRequired["str"]
    """<p>The name of the Amazon Web Services Glue connection.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon Web Services Glue connection.</p>"""
    connection_type: NotRequired[
        "aws_sdk_datazone.types.glue_connection_type.GlueConnectionType"
    ]
    """<p>The connection type of the Amazon Web Services Glue connection.</p>"""
    match_criteria: NotRequired["str"]
    """<p>The match criteria of the Amazon Web Services Glue connection.</p>"""
    validate_credentials: NotRequired["bool"]
    """<p>Speciefies whether to validate credentials of the Amazon Web Services Glue connection.</p>"""
    validate_for_compute_environments: NotRequired[
        "aws_sdk_datazone.types.compute_environments_list.ComputeEnvironmentsList"
    ]
    """<p>Speciefies whether to validate for compute environments of the Amazon Web Services Glue connection.</p>"""
    spark_properties: NotRequired["aws_sdk_datazone.types.property_map.PropertyMap"]
    """<p>The Spark properties of the Amazon Web Services Glue connection.</p>"""
    athena_properties: NotRequired["aws_sdk_datazone.types.property_map.PropertyMap"]
    """<p>The Amazon Athena properties of the Amazon Web Services Glue connection.</p>"""
    python_properties: NotRequired["aws_sdk_datazone.types.property_map.PropertyMap"]
    """<p>The Python properties of the Amazon Web Services Glue connection.</p>"""
    authentication_configuration: NotRequired[
        "aws_sdk_datazone.types.authentication_configuration_input.AuthenticationConfigurationInput"
    ]
    """<p>The authentication configuration of the Amazon Web Services Glue connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueConnectionInput) -> dict:
    out: dict = {}
    if "connection_properties" in value:
        import aws_sdk_datazone.types.connection_properties

        out["connectionProperties"] = (
            aws_sdk_datazone.types.connection_properties.serialize_json(
                value["connection_properties"]
            )
        )
    if "physical_connection_requirements" in value:
        import aws_sdk_datazone.types.physical_connection_requirements

        out["physicalConnectionRequirements"] = (
            aws_sdk_datazone.types.physical_connection_requirements.serialize_json(
                value["physical_connection_requirements"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "connection_type" in value:
        import aws_sdk_datazone.types.glue_connection_type

        out["connectionType"] = (
            aws_sdk_datazone.types.glue_connection_type.serialize_json(
                value["connection_type"]
            )
        )
    if "match_criteria" in value:
        out["matchCriteria"] = value["match_criteria"]
    if "validate_credentials" in value:
        out["validateCredentials"] = value["validate_credentials"]
    if "validate_for_compute_environments" in value:
        import aws_sdk_datazone.types.compute_environments_list

        out["validateForComputeEnvironments"] = (
            aws_sdk_datazone.types.compute_environments_list.serialize_json(
                value["validate_for_compute_environments"]
            )
        )
    if "spark_properties" in value:
        import aws_sdk_datazone.types.property_map

        out["sparkProperties"] = aws_sdk_datazone.types.property_map.serialize_json(
            value["spark_properties"]
        )
    if "athena_properties" in value:
        import aws_sdk_datazone.types.property_map

        out["athenaProperties"] = aws_sdk_datazone.types.property_map.serialize_json(
            value["athena_properties"]
        )
    if "python_properties" in value:
        import aws_sdk_datazone.types.property_map

        out["pythonProperties"] = aws_sdk_datazone.types.property_map.serialize_json(
            value["python_properties"]
        )
    if "authentication_configuration" in value:
        import aws_sdk_datazone.types.authentication_configuration_input

        out["authenticationConfiguration"] = (
            aws_sdk_datazone.types.authentication_configuration_input.serialize_json(
                value["authentication_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlueConnectionInput:
    out: GlueConnectionInput = {}  # type: ignore[typeddict-item]
    if "connectionProperties" in data:
        import aws_sdk_datazone.types.connection_properties

        out["connection_properties"] = (
            aws_sdk_datazone.types.connection_properties.deserialize_json(
                data["connectionProperties"]
            )
        )
    if "physicalConnectionRequirements" in data:
        import aws_sdk_datazone.types.physical_connection_requirements

        out["physical_connection_requirements"] = (
            aws_sdk_datazone.types.physical_connection_requirements.deserialize_json(
                data["physicalConnectionRequirements"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "connectionType" in data:
        import aws_sdk_datazone.types.glue_connection_type

        out["connection_type"] = (
            aws_sdk_datazone.types.glue_connection_type.deserialize_json(
                data["connectionType"]
            )
        )
    if "matchCriteria" in data:
        out["match_criteria"] = data["matchCriteria"]
    if "validateCredentials" in data:
        out["validate_credentials"] = data["validateCredentials"]
    if "validateForComputeEnvironments" in data:
        import aws_sdk_datazone.types.compute_environments_list

        out["validate_for_compute_environments"] = (
            aws_sdk_datazone.types.compute_environments_list.deserialize_json(
                data["validateForComputeEnvironments"]
            )
        )
    if "sparkProperties" in data:
        import aws_sdk_datazone.types.property_map

        out["spark_properties"] = aws_sdk_datazone.types.property_map.deserialize_json(
            data["sparkProperties"]
        )
    if "athenaProperties" in data:
        import aws_sdk_datazone.types.property_map

        out["athena_properties"] = aws_sdk_datazone.types.property_map.deserialize_json(
            data["athenaProperties"]
        )
    if "pythonProperties" in data:
        import aws_sdk_datazone.types.property_map

        out["python_properties"] = aws_sdk_datazone.types.property_map.deserialize_json(
            data["pythonProperties"]
        )
    if "authenticationConfiguration" in data:
        import aws_sdk_datazone.types.authentication_configuration_input

        out["authentication_configuration"] = (
            aws_sdk_datazone.types.authentication_configuration_input.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    return out
