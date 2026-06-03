"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.string_set_attribute_value
    import aws_sdk_dynamodb.types.number_attribute_value
    import aws_sdk_dynamodb.types.null_attribute_value
    import aws_sdk_dynamodb.types.boolean_attribute_value
    import aws_sdk_dynamodb.types.list_attribute_value
    import aws_sdk_dynamodb.types.binary_set_attribute_value
    import aws_sdk_dynamodb.types.number_set_attribute_value
    import aws_sdk_dynamodb.types.string_attribute_value
    import aws_sdk_dynamodb.types.map_attribute_value
    import aws_sdk_dynamodb.types.binary_attribute_value


class _AttributeValue_S(TypedDict):
    S: "aws_sdk_dynamodb.types.string_attribute_value.StringAttributeValue"


class _AttributeValue_N(TypedDict):
    N: "aws_sdk_dynamodb.types.number_attribute_value.NumberAttributeValue"


class _AttributeValue_B(TypedDict):
    B: "aws_sdk_dynamodb.types.binary_attribute_value.BinaryAttributeValue"


class _AttributeValue_SS(TypedDict):
    SS: "aws_sdk_dynamodb.types.string_set_attribute_value.StringSetAttributeValue"


class _AttributeValue_NS(TypedDict):
    NS: "aws_sdk_dynamodb.types.number_set_attribute_value.NumberSetAttributeValue"


class _AttributeValue_BS(TypedDict):
    BS: "aws_sdk_dynamodb.types.binary_set_attribute_value.BinarySetAttributeValue"


class _AttributeValue_M(TypedDict):
    M: "aws_sdk_dynamodb.types.map_attribute_value.MapAttributeValue"


class _AttributeValue_L(TypedDict):
    L: "aws_sdk_dynamodb.types.list_attribute_value.ListAttributeValue"


class _AttributeValue_NULL(TypedDict):
    NULL: "aws_sdk_dynamodb.types.null_attribute_value.NullAttributeValue"


class _AttributeValue_BOOL(TypedDict):
    BOOL: "aws_sdk_dynamodb.types.boolean_attribute_value.BooleanAttributeValue"


AttributeValue: TypeAlias = (
    _AttributeValue_S
    | _AttributeValue_N
    | _AttributeValue_B
    | _AttributeValue_SS
    | _AttributeValue_NS
    | _AttributeValue_BS
    | _AttributeValue_M
    | _AttributeValue_L
    | _AttributeValue_NULL
    | _AttributeValue_BOOL
)
