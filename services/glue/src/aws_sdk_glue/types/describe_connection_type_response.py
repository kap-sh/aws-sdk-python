"""Generated from Smithy shape ``com.amazonaws.glue#DescribeConnectionTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.auth_configuration
    import aws_sdk_glue.types.capabilities
    import aws_sdk_glue.types.compute_environment_configuration_map
    import aws_sdk_glue.types.description
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.properties_map
    import aws_sdk_glue.types.rest_configuration


class DescribeConnectionTypeResponse(TypedDict):
    connection_type: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the connection type.</p>"""
    description: NotRequired["aws_sdk_glue.types.description.Description"]
    """<p>A description of the connection type.</p>"""
    capabilities: NotRequired["aws_sdk_glue.types.capabilities.Capabilities"]
    """<p>The supported authentication types, data interface types (compute environments), and data operations of the connector.</p>"""
    connection_properties: NotRequired[
        "aws_sdk_glue.types.properties_map.PropertiesMap"
    ]
    """<p>Connection properties which are common across compute environments.</p>"""
    connection_options: NotRequired["aws_sdk_glue.types.properties_map.PropertiesMap"]
    """<p>Returns properties that can be set when creating a connection in the <code>ConnectionInput.ConnectionProperties</code>. <code>ConnectionOptions</code> defines parameters that can be set in a Spark ETL script in the connection options map passed to a dataframe.</p>"""
    authentication_configuration: NotRequired[
        "aws_sdk_glue.types.auth_configuration.AuthConfiguration"
    ]
    """<p>The type of authentication used for the connection.</p>"""
    compute_environment_configurations: NotRequired[
        "aws_sdk_glue.types.compute_environment_configuration_map.ComputeEnvironmentConfigurationMap"
    ]
    """<p>The compute environments that are supported by the connection.</p>"""
    physical_connection_requirements: NotRequired[
        "aws_sdk_glue.types.properties_map.PropertiesMap"
    ]
    """<p>Physical requirements for a connection, such as VPC, Subnet and Security Group specifications.</p>"""
    athena_connection_properties: NotRequired[
        "aws_sdk_glue.types.properties_map.PropertiesMap"
    ]
    """<p>Connection properties specific to the Athena compute environment.</p>"""
    python_connection_properties: NotRequired[
        "aws_sdk_glue.types.properties_map.PropertiesMap"
    ]
    """<p>Connection properties specific to the Python compute environment.</p>"""
    spark_connection_properties: NotRequired[
        "aws_sdk_glue.types.properties_map.PropertiesMap"
    ]
    """<p>Connection properties specific to the Spark compute environment.</p>"""
    rest_configuration: NotRequired[
        "aws_sdk_glue.types.rest_configuration.RestConfiguration"
    ]
    """<p>HTTP request and response configuration, validation endpoint, and entity configurations for REST based data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionTypeResponse) -> dict:
    out: dict = {}
    if "connection_type" in value:
        out["ConnectionType"] = value["connection_type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "capabilities" in value:
        import aws_sdk_glue.types.capabilities

        out["Capabilities"] = aws_sdk_glue.types.capabilities.serialize_aws_json_1_1(
            value["capabilities"]
        )
    if "connection_properties" in value:
        import aws_sdk_glue.types.properties_map

        out["ConnectionProperties"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["connection_properties"]
            )
        )
    if "connection_options" in value:
        import aws_sdk_glue.types.properties_map

        out["ConnectionOptions"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["connection_options"]
            )
        )
    if "authentication_configuration" in value:
        import aws_sdk_glue.types.auth_configuration

        out["AuthenticationConfiguration"] = (
            aws_sdk_glue.types.auth_configuration.serialize_aws_json_1_1(
                value["authentication_configuration"]
            )
        )
    if "compute_environment_configurations" in value:
        import aws_sdk_glue.types.compute_environment_configuration_map

        out["ComputeEnvironmentConfigurations"] = (
            aws_sdk_glue.types.compute_environment_configuration_map.serialize_aws_json_1_1(
                value["compute_environment_configurations"]
            )
        )
    if "physical_connection_requirements" in value:
        import aws_sdk_glue.types.properties_map

        out["PhysicalConnectionRequirements"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["physical_connection_requirements"]
            )
        )
    if "athena_connection_properties" in value:
        import aws_sdk_glue.types.properties_map

        out["AthenaConnectionProperties"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["athena_connection_properties"]
            )
        )
    if "python_connection_properties" in value:
        import aws_sdk_glue.types.properties_map

        out["PythonConnectionProperties"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["python_connection_properties"]
            )
        )
    if "spark_connection_properties" in value:
        import aws_sdk_glue.types.properties_map

        out["SparkConnectionProperties"] = (
            aws_sdk_glue.types.properties_map.serialize_aws_json_1_1(
                value["spark_connection_properties"]
            )
        )
    if "rest_configuration" in value:
        import aws_sdk_glue.types.rest_configuration

        out["RestConfiguration"] = (
            aws_sdk_glue.types.rest_configuration.serialize_aws_json_1_1(
                value["rest_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionTypeResponse:
    out: DescribeConnectionTypeResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Capabilities" in data:
        import aws_sdk_glue.types.capabilities

        out["capabilities"] = aws_sdk_glue.types.capabilities.deserialize_aws_json_1_1(
            data["Capabilities"]
        )
    if "ConnectionProperties" in data:
        import aws_sdk_glue.types.properties_map

        out["connection_properties"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["ConnectionProperties"]
            )
        )
    if "ConnectionOptions" in data:
        import aws_sdk_glue.types.properties_map

        out["connection_options"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["ConnectionOptions"]
            )
        )
    if "AuthenticationConfiguration" in data:
        import aws_sdk_glue.types.auth_configuration

        out["authentication_configuration"] = (
            aws_sdk_glue.types.auth_configuration.deserialize_aws_json_1_1(
                data["AuthenticationConfiguration"]
            )
        )
    if "ComputeEnvironmentConfigurations" in data:
        import aws_sdk_glue.types.compute_environment_configuration_map

        out["compute_environment_configurations"] = (
            aws_sdk_glue.types.compute_environment_configuration_map.deserialize_aws_json_1_1(
                data["ComputeEnvironmentConfigurations"]
            )
        )
    if "PhysicalConnectionRequirements" in data:
        import aws_sdk_glue.types.properties_map

        out["physical_connection_requirements"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["PhysicalConnectionRequirements"]
            )
        )
    if "AthenaConnectionProperties" in data:
        import aws_sdk_glue.types.properties_map

        out["athena_connection_properties"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["AthenaConnectionProperties"]
            )
        )
    if "PythonConnectionProperties" in data:
        import aws_sdk_glue.types.properties_map

        out["python_connection_properties"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["PythonConnectionProperties"]
            )
        )
    if "SparkConnectionProperties" in data:
        import aws_sdk_glue.types.properties_map

        out["spark_connection_properties"] = (
            aws_sdk_glue.types.properties_map.deserialize_aws_json_1_1(
                data["SparkConnectionProperties"]
            )
        )
    if "RestConfiguration" in data:
        import aws_sdk_glue.types.rest_configuration

        out["rest_configuration"] = (
            aws_sdk_glue.types.rest_configuration.deserialize_aws_json_1_1(
                data["RestConfiguration"]
            )
        )
    return out
