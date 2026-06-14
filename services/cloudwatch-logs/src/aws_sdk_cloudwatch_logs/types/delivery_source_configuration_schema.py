"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceConfigurationSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_numeric_value
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_field
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_value_type
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_supported_values


class DeliverySourceConfigurationSchema(TypedDict):
    key_name: "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_field.DeliverySourceConfigurationSchemaField"
    """<p>The name of the configuration.</p>"""
    value_type: "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_value_type.DeliverySourceConfigurationSchemaValueType"
    """<p>The data type of the configuration value. Valid values are <code>string</code>, <code>boolean</code>, <code>int</code>, <code>double</code>, and <code>long</code>.</p>"""
    default_value: "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_field.DeliverySourceConfigurationSchemaField"
    """<p>The default value of the configuration that is used when a value is not specified in a <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html\">PutDeliverySource</a> request.</p>"""
    supported_values: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_supported_values.DeliverySourceConfigurationSupportedValues"
    ]
    """<p>The list of allowed values for the configuration. Empty for free-form configuration.</p>"""
    min_value: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_numeric_value.DeliverySourceConfigurationNumericValue"
    ]
    """<p>The minimum numeric value allowed for the configuration. This applies only when the <code>valueType</code> is a numeric type.</p>"""
    max_value: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_source_configuration_numeric_value.DeliverySourceConfigurationNumericValue"
    ]
    """<p>The maximum numeric value allowed for the configuration. This applies only when the <code>valueType</code> is a numeric type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySourceConfigurationSchema) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_value_type

    out["valueType"] = (
        aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_value_type.serialize_aws_json_1_1(
            value["value_type"]
        )
    )
    out["defaultValue"] = value["default_value"]
    if "supported_values" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_supported_values

        out["supportedValues"] = (
            aws_sdk_cloudwatch_logs.types.delivery_source_configuration_supported_values.serialize_aws_json_1_1(
                value["supported_values"]
            )
        )
    if "min_value" in value:
        out["minValue"] = value["min_value"]
    if "max_value" in value:
        out["maxValue"] = value["max_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliverySourceConfigurationSchema:
    out: DeliverySourceConfigurationSchema = {}  # type: ignore[typeddict-item]
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    else:
        raise DeserializationError(
            "DeliverySourceConfigurationSchema.key_name required"
        )
    if "valueType" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_value_type

        out["value_type"] = (
            aws_sdk_cloudwatch_logs.types.delivery_source_configuration_schema_value_type.deserialize_aws_json_1_1(
                data["valueType"]
            )
        )
    else:
        raise DeserializationError(
            "DeliverySourceConfigurationSchema.value_type required"
        )
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    else:
        raise DeserializationError(
            "DeliverySourceConfigurationSchema.default_value required"
        )
    if "supportedValues" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_source_configuration_supported_values

        out["supported_values"] = (
            aws_sdk_cloudwatch_logs.types.delivery_source_configuration_supported_values.deserialize_aws_json_1_1(
                data["supportedValues"]
            )
        )
    if "minValue" in data:
        out["min_value"] = data["minValue"]
    if "maxValue" in data:
        out["max_value"] = data["maxValue"]
    return out
