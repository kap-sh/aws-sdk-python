"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ConfigurationTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.allowed_action_for_allow_vended_logs_delivery_for_resource
    import aws_sdk_cloudwatch_logs.types.allowed_field_delimiters
    import aws_sdk_cloudwatch_logs.types.allowed_fields
    import aws_sdk_cloudwatch_logs.types.configuration_template_delivery_config_values
    import aws_sdk_cloudwatch_logs.types.delivery_destination_type
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schemas
    import aws_sdk_cloudwatch_logs.types.log_type
    import aws_sdk_cloudwatch_logs.types.output_formats
    import aws_sdk_cloudwatch_logs.types.record_fields
    import aws_sdk_cloudwatch_logs.types.resource_type
    import aws_sdk_cloudwatch_logs.types.s3_tables_integration
    import aws_sdk_cloudwatch_logs.types.service


class ConfigurationTemplate(TypedDict):
    service: NotRequired["aws_sdk_cloudwatch_logs.types.service.Service"]
    """<p>A string specifying which service this configuration template applies to. For more information about supported services see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html\">Enable logging from Amazon Web Services services.</a>.</p>"""
    log_type: NotRequired["aws_sdk_cloudwatch_logs.types.log_type.LogType"]
    """<p>A string specifying which log type this configuration template applies to.</p>"""
    resource_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.resource_type.ResourceType"
    ]
    """<p>A string specifying which resource type this configuration template applies to.</p>"""
    delivery_destination_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>A string specifying which destination type this configuration template applies to.</p>"""
    default_delivery_config_values: NotRequired[
        "aws_sdk_cloudwatch_logs.types.configuration_template_delivery_config_values.ConfigurationTemplateDeliveryConfigValues"
    ]
    """<p>A mapping that displays the default value of each property within a delivery's configuration, if it is not specified in the request.</p>"""
    allowed_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.allowed_fields.AllowedFields"
    ]
    """<p>The allowed fields that a caller can use in the <code>recordFields</code> parameter of a <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html\">CreateDelivery</a> or <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html\">UpdateDeliveryConfiguration</a> operation.</p>"""
    allowed_output_formats: NotRequired[
        "aws_sdk_cloudwatch_logs.types.output_formats.OutputFormats"
    ]
    """<p>The list of delivery destination output formats that are supported by this log source.</p>"""
    allowed_action_for_allow_vended_logs_delivery_for_resource: NotRequired[
        "aws_sdk_cloudwatch_logs.types.allowed_action_for_allow_vended_logs_delivery_for_resource.AllowedActionForAllowVendedLogsDeliveryForResource"
    ]
    """<p>The action permissions that a caller needs to have to be able to successfully create a delivery source on the desired resource type when calling <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html\">PutDeliverySource</a>.</p>"""
    allowed_field_delimiters: NotRequired[
        "aws_sdk_cloudwatch_logs.types.allowed_field_delimiters.AllowedFieldDelimiters"
    ]
    """<p>The valid values that a caller can use as field delimiters when calling <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html\">CreateDelivery</a> or <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html\">UpdateDeliveryConfiguration</a> on a delivery that delivers in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>"""
    allowed_suffix_path_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.record_fields.RecordFields"
    ]
    """<p>The list of variable fields that can be used in the suffix path of a delivery that delivers to an S3 bucket.</p>"""
    delivery_source_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schemas.DeliverySourceConfigurationSchemas"
    ]
    """<p>The schema of the delivery source configuration that is available for this log type. Each element describes a configuration that can be set when calling <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html\">PutDeliverySource</a>, including the configuration name, type, and default value.</p>"""
    s3_tables_integration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.s3_tables_integration.S3TablesIntegration"
    ]
    """<p>The S3 Tables integration configuration for this configuration template, including the datasource name and type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTemplate) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "log_type" in value:
        out["logType"] = value["log_type"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "delivery_destination_type" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["deliveryDestinationType"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.serialize_aws_json_1_1(
                value["delivery_destination_type"]
            )
        )
    if "default_delivery_config_values" in value:
        import aws_sdk_cloudwatch_logs.types.configuration_template_delivery_config_values

        out["defaultDeliveryConfigValues"] = (
            aws_sdk_cloudwatch_logs.types.configuration_template_delivery_config_values.serialize_aws_json_1_1(
                value["default_delivery_config_values"]
            )
        )
    if "allowed_fields" in value:
        import aws_sdk_cloudwatch_logs.types.allowed_fields

        out["allowedFields"] = (
            aws_sdk_cloudwatch_logs.types.allowed_fields.serialize_aws_json_1_1(
                value["allowed_fields"]
            )
        )
    if "allowed_output_formats" in value:
        import aws_sdk_cloudwatch_logs.types.output_formats

        out["allowedOutputFormats"] = (
            aws_sdk_cloudwatch_logs.types.output_formats.serialize_aws_json_1_1(
                value["allowed_output_formats"]
            )
        )
    if "allowed_action_for_allow_vended_logs_delivery_for_resource" in value:
        out["allowedActionForAllowVendedLogsDeliveryForResource"] = value[
            "allowed_action_for_allow_vended_logs_delivery_for_resource"
        ]
    if "allowed_field_delimiters" in value:
        import aws_sdk_cloudwatch_logs.types.allowed_field_delimiters

        out["allowedFieldDelimiters"] = (
            aws_sdk_cloudwatch_logs.types.allowed_field_delimiters.serialize_aws_json_1_1(
                value["allowed_field_delimiters"]
            )
        )
    if "allowed_suffix_path_fields" in value:
        import aws_sdk_cloudwatch_logs.types.record_fields

        out["allowedSuffixPathFields"] = (
            aws_sdk_cloudwatch_logs.types.record_fields.serialize_aws_json_1_1(
                value["allowed_suffix_path_fields"]
            )
        )
    if "delivery_source_configuration" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schemas

        out["deliverySourceConfiguration"] = (
            aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schemas.serialize_aws_json_1_1(
                value["delivery_source_configuration"]
            )
        )
    if "s3_tables_integration" in value:
        import aws_sdk_cloudwatch_logs.types.s3_tables_integration

        out["s3TablesIntegration"] = (
            aws_sdk_cloudwatch_logs.types.s3_tables_integration.serialize_aws_json_1_1(
                value["s3_tables_integration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationTemplate:
    out: ConfigurationTemplate = {}  # type: ignore[typeddict-item]
    if "service" in data:
        out["service"] = data["service"]
    if "logType" in data:
        out["log_type"] = data["logType"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "deliveryDestinationType" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["delivery_destination_type"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.deserialize_aws_json_1_1(
                data["deliveryDestinationType"]
            )
        )
    if "defaultDeliveryConfigValues" in data:
        import aws_sdk_cloudwatch_logs.types.configuration_template_delivery_config_values

        out["default_delivery_config_values"] = (
            aws_sdk_cloudwatch_logs.types.configuration_template_delivery_config_values.deserialize_aws_json_1_1(
                data["defaultDeliveryConfigValues"]
            )
        )
    if "allowedFields" in data:
        import aws_sdk_cloudwatch_logs.types.allowed_fields

        out["allowed_fields"] = (
            aws_sdk_cloudwatch_logs.types.allowed_fields.deserialize_aws_json_1_1(
                data["allowedFields"]
            )
        )
    if "allowedOutputFormats" in data:
        import aws_sdk_cloudwatch_logs.types.output_formats

        out["allowed_output_formats"] = (
            aws_sdk_cloudwatch_logs.types.output_formats.deserialize_aws_json_1_1(
                data["allowedOutputFormats"]
            )
        )
    if "allowedActionForAllowVendedLogsDeliveryForResource" in data:
        out["allowed_action_for_allow_vended_logs_delivery_for_resource"] = data[
            "allowedActionForAllowVendedLogsDeliveryForResource"
        ]
    if "allowedFieldDelimiters" in data:
        import aws_sdk_cloudwatch_logs.types.allowed_field_delimiters

        out["allowed_field_delimiters"] = (
            aws_sdk_cloudwatch_logs.types.allowed_field_delimiters.deserialize_aws_json_1_1(
                data["allowedFieldDelimiters"]
            )
        )
    if "allowedSuffixPathFields" in data:
        import aws_sdk_cloudwatch_logs.types.record_fields

        out["allowed_suffix_path_fields"] = (
            aws_sdk_cloudwatch_logs.types.record_fields.deserialize_aws_json_1_1(
                data["allowedSuffixPathFields"]
            )
        )
    if "deliverySourceConfiguration" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schemas

        out["delivery_source_configuration"] = (
            aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schemas.deserialize_aws_json_1_1(
                data["deliverySourceConfiguration"]
            )
        )
    if "s3TablesIntegration" in data:
        import aws_sdk_cloudwatch_logs.types.s3_tables_integration

        out["s3_tables_integration"] = (
            aws_sdk_cloudwatch_logs.types.s3_tables_integration.deserialize_aws_json_1_1(
                data["s3TablesIntegration"]
            )
        )
    return out
