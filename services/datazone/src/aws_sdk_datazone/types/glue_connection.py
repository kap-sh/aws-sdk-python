"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnection``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.authentication_configuration
    import aws_sdk_datazone.types.compute_environments_list
    import aws_sdk_datazone.types.connection_properties
    import aws_sdk_datazone.types.connection_status
    import aws_sdk_datazone.types.connection_type
    import aws_sdk_datazone.types.match_criteria
    import aws_sdk_datazone.types.physical_connection_requirements
    import aws_sdk_datazone.types.property_map
    import datetime


class GlueConnection(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the Amazon Web Services Glue connection.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon Web Services Glue connection.</p>"""
    connection_type: NotRequired[
        "aws_sdk_datazone.types.connection_type.ConnectionType"
    ]
    """<p>The type of the Amazon Web Services Glue connection.</p>"""
    match_criteria: NotRequired["aws_sdk_datazone.types.match_criteria.MatchCriteria"]
    """<p>The match criteria of the Amazon Web Services Glue connection.</p>"""
    connection_properties: NotRequired[
        "aws_sdk_datazone.types.connection_properties.ConnectionProperties"
    ]
    """<p>The properties of the Amazon Web Services Glue connection.</p>"""
    spark_properties: NotRequired["aws_sdk_datazone.types.property_map.PropertyMap"]
    """<p>The Spark properties of the Amazon Web Services Glue connection.</p>"""
    athena_properties: NotRequired["aws_sdk_datazone.types.property_map.PropertyMap"]
    """<p>The Amazon Athena properties of the Amazon Web Services Glue connection.</p>"""
    python_properties: NotRequired["aws_sdk_datazone.types.property_map.PropertyMap"]
    """<p>The Python properties of the Amazon Web Services Glue connection.</p>"""
    physical_connection_requirements: NotRequired[
        "aws_sdk_datazone.types.physical_connection_requirements.PhysicalConnectionRequirements"
    ]
    """<p>The physical connection requirements of the Amazon Web Services Glue connection.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The creation time of the Amazon Web Services Glue connection.</p>"""
    last_updated_time: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the Amazon Web Services Glue connection was last updated.</p>"""
    last_updated_by: NotRequired["str"]
    """<p>The user who last updated the Amazon Web Services Glue connection.</p>"""
    status: NotRequired["aws_sdk_datazone.types.connection_status.ConnectionStatus"]
    """<p>The status of the Amazon Web Services Glue connection.</p>"""
    status_reason: NotRequired["str"]
    """<p>The status reason of the Amazon Web Services Glue connection.</p>"""
    last_connection_validation_time: NotRequired["datetime.datetime"]
    """<p>The last validation time of the Amazon Web Services Glue connection.</p>"""
    authentication_configuration: NotRequired[
        "aws_sdk_datazone.types.authentication_configuration.AuthenticationConfiguration"
    ]
    """<p>The authentication configuration of the Amazon Web Services Glue connection.</p>"""
    connection_schema_version: NotRequired["int"]
    """<p>The connection schema version of the Amazon Web Services Glue connection.</p>"""
    compatible_compute_environments: NotRequired[
        "aws_sdk_datazone.types.compute_environments_list.ComputeEnvironmentsList"
    ]
    """<p>The compatible compute environments of the Amazon Web Services Glue connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueConnection) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "connection_type" in value:
        import aws_sdk_datazone.types.connection_type

        out["connectionType"] = aws_sdk_datazone.types.connection_type.serialize_json(
            value["connection_type"]
        )
    if "match_criteria" in value:
        import aws_sdk_datazone.types.match_criteria

        out["matchCriteria"] = aws_sdk_datazone.types.match_criteria.serialize_json(
            value["match_criteria"]
        )
    if "connection_properties" in value:
        import aws_sdk_datazone.types.connection_properties

        out["connectionProperties"] = (
            aws_sdk_datazone.types.connection_properties.serialize_json(
                value["connection_properties"]
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
    if "physical_connection_requirements" in value:
        import aws_sdk_datazone.types.physical_connection_requirements

        out["physicalConnectionRequirements"] = (
            aws_sdk_datazone.types.physical_connection_requirements.serialize_json(
                value["physical_connection_requirements"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["creationTime"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lastUpdatedTime"] = (
            aws_sdk_datazone.types._prelude.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "status" in value:
        import aws_sdk_datazone.types.connection_status

        out["status"] = aws_sdk_datazone.types.connection_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_connection_validation_time" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lastConnectionValidationTime"] = (
            aws_sdk_datazone.types._prelude.timestamp.serialize_json(
                value["last_connection_validation_time"]
            )
        )
    if "authentication_configuration" in value:
        import aws_sdk_datazone.types.authentication_configuration

        out["authenticationConfiguration"] = (
            aws_sdk_datazone.types.authentication_configuration.serialize_json(
                value["authentication_configuration"]
            )
        )
    if "connection_schema_version" in value:
        out["connectionSchemaVersion"] = value["connection_schema_version"]
    if "compatible_compute_environments" in value:
        import aws_sdk_datazone.types.compute_environments_list

        out["compatibleComputeEnvironments"] = (
            aws_sdk_datazone.types.compute_environments_list.serialize_json(
                value["compatible_compute_environments"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlueConnection:
    out: GlueConnection = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "connectionType" in data:
        import aws_sdk_datazone.types.connection_type

        out["connection_type"] = (
            aws_sdk_datazone.types.connection_type.deserialize_json(
                data["connectionType"]
            )
        )
    if "matchCriteria" in data:
        import aws_sdk_datazone.types.match_criteria

        out["match_criteria"] = aws_sdk_datazone.types.match_criteria.deserialize_json(
            data["matchCriteria"]
        )
    if "connectionProperties" in data:
        import aws_sdk_datazone.types.connection_properties

        out["connection_properties"] = (
            aws_sdk_datazone.types.connection_properties.deserialize_json(
                data["connectionProperties"]
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
    if "physicalConnectionRequirements" in data:
        import aws_sdk_datazone.types.physical_connection_requirements

        out["physical_connection_requirements"] = (
            aws_sdk_datazone.types.physical_connection_requirements.deserialize_json(
                data["physicalConnectionRequirements"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["last_updated_time"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "status" in data:
        import aws_sdk_datazone.types.connection_status

        out["status"] = aws_sdk_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "lastConnectionValidationTime" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["last_connection_validation_time"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["lastConnectionValidationTime"]
            )
        )
    if "authenticationConfiguration" in data:
        import aws_sdk_datazone.types.authentication_configuration

        out["authentication_configuration"] = (
            aws_sdk_datazone.types.authentication_configuration.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    if "connectionSchemaVersion" in data:
        out["connection_schema_version"] = data["connectionSchemaVersion"]
    if "compatibleComputeEnvironments" in data:
        import aws_sdk_datazone.types.compute_environments_list

        out["compatible_compute_environments"] = (
            aws_sdk_datazone.types.compute_environments_list.deserialize_json(
                data["compatibleComputeEnvironments"]
            )
        )
    return out
