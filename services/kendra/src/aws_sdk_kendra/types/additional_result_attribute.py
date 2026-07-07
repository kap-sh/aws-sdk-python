"""Generated from Smithy shape ``com.amazonaws.kendra#AdditionalResultAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.additional_result_attribute_value
    import aws_sdk_kendra.types.additional_result_attribute_value_type
    import aws_sdk_kendra.types.string


class AdditionalResultAttribute(TypedDict, closed=True):
    key: "aws_sdk_kendra.types.string.String"
    """<p>The key that identifies the attribute.</p>"""
    value_type: "aws_sdk_kendra.types.additional_result_attribute_value_type.AdditionalResultAttributeValueType"
    """<p>The data type of the <code>Value</code> property.</p>"""
    value: "aws_sdk_kendra.types.additional_result_attribute_value.AdditionalResultAttributeValue"
    """<p>An object that contains the attribute value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalResultAttribute) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_kendra.types.additional_result_attribute_value_type

    out["ValueType"] = (
        aws_sdk_kendra.types.additional_result_attribute_value_type.serialize_aws_json_1_1(
            value["value_type"]
        )
    )
    import aws_sdk_kendra.types.additional_result_attribute_value

    out["Value"] = (
        aws_sdk_kendra.types.additional_result_attribute_value.serialize_aws_json_1_1(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalResultAttribute:
    out: AdditionalResultAttribute = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("AdditionalResultAttribute.key required")
    if "ValueType" in data:
        import aws_sdk_kendra.types.additional_result_attribute_value_type

        out["value_type"] = (
            aws_sdk_kendra.types.additional_result_attribute_value_type.deserialize_aws_json_1_1(
                data["ValueType"]
            )
        )
    else:
        raise DeserializationError("AdditionalResultAttribute.value_type required")
    if "Value" in data:
        import aws_sdk_kendra.types.additional_result_attribute_value

        out["value"] = (
            aws_sdk_kendra.types.additional_result_attribute_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("AdditionalResultAttribute.value required")
    return out
