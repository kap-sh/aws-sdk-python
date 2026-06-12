"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#AttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_dynamodb_streams.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.binary_attribute_value
    import aws_sdk_dynamodb_streams.types.binary_set_attribute_value
    import aws_sdk_dynamodb_streams.types.boolean_attribute_value
    import aws_sdk_dynamodb_streams.types.list_attribute_value
    import aws_sdk_dynamodb_streams.types.map_attribute_value
    import aws_sdk_dynamodb_streams.types.null_attribute_value
    import aws_sdk_dynamodb_streams.types.number_attribute_value
    import aws_sdk_dynamodb_streams.types.number_set_attribute_value
    import aws_sdk_dynamodb_streams.types.string_attribute_value
    import aws_sdk_dynamodb_streams.types.string_set_attribute_value


class _AttributeValue_S(TypedDict):
    S: "aws_sdk_dynamodb_streams.types.string_attribute_value.StringAttributeValue"


class _AttributeValue_N(TypedDict):
    N: "aws_sdk_dynamodb_streams.types.number_attribute_value.NumberAttributeValue"


class _AttributeValue_B(TypedDict):
    B: "aws_sdk_dynamodb_streams.types.binary_attribute_value.BinaryAttributeValue"


class _AttributeValue_SS(TypedDict):
    SS: "aws_sdk_dynamodb_streams.types.string_set_attribute_value.StringSetAttributeValue"


class _AttributeValue_NS(TypedDict):
    NS: "aws_sdk_dynamodb_streams.types.number_set_attribute_value.NumberSetAttributeValue"


class _AttributeValue_BS(TypedDict):
    BS: "aws_sdk_dynamodb_streams.types.binary_set_attribute_value.BinarySetAttributeValue"


class _AttributeValue_M(TypedDict):
    M: "aws_sdk_dynamodb_streams.types.map_attribute_value.MapAttributeValue"


class _AttributeValue_L(TypedDict):
    L: "aws_sdk_dynamodb_streams.types.list_attribute_value.ListAttributeValue"


class _AttributeValue_NULL(TypedDict):
    NULL: "aws_sdk_dynamodb_streams.types.null_attribute_value.NullAttributeValue"


class _AttributeValue_BOOL(TypedDict):
    BOOL: "aws_sdk_dynamodb_streams.types.boolean_attribute_value.BooleanAttributeValue"


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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeValue) -> dict:
    if "S" in value:
        return {"S": value["S"]}
    elif "N" in value:
        return {"N": value["N"]}
    elif "B" in value:
        import aws_sdk_dynamodb_streams.types.binary_attribute_value

        return {
            "B": aws_sdk_dynamodb_streams.types.binary_attribute_value.serialize_aws_json_1_0(
                value["B"]
            )
        }
    elif "SS" in value:
        import aws_sdk_dynamodb_streams.types.string_set_attribute_value

        return {
            "SS": aws_sdk_dynamodb_streams.types.string_set_attribute_value.serialize_aws_json_1_0(
                value["SS"]
            )
        }
    elif "NS" in value:
        import aws_sdk_dynamodb_streams.types.number_set_attribute_value

        return {
            "NS": aws_sdk_dynamodb_streams.types.number_set_attribute_value.serialize_aws_json_1_0(
                value["NS"]
            )
        }
    elif "BS" in value:
        import aws_sdk_dynamodb_streams.types.binary_set_attribute_value

        return {
            "BS": aws_sdk_dynamodb_streams.types.binary_set_attribute_value.serialize_aws_json_1_0(
                value["BS"]
            )
        }
    elif "M" in value:
        import aws_sdk_dynamodb_streams.types.map_attribute_value

        return {
            "M": aws_sdk_dynamodb_streams.types.map_attribute_value.serialize_aws_json_1_0(
                value["M"]
            )
        }
    elif "L" in value:
        import aws_sdk_dynamodb_streams.types.list_attribute_value

        return {
            "L": aws_sdk_dynamodb_streams.types.list_attribute_value.serialize_aws_json_1_0(
                value["L"]
            )
        }
    elif "NULL" in value:
        return {"NULL": value["NULL"]}
    elif "BOOL" in value:
        return {"BOOL": value["BOOL"]}
    else:
        raise SerializationError("AttributeValue: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AttributeValue:
    if "S" in data:
        return {"S": data["S"]}
    elif "N" in data:
        return {"N": data["N"]}
    elif "B" in data:
        import aws_sdk_dynamodb_streams.types.binary_attribute_value

        return {
            "B": aws_sdk_dynamodb_streams.types.binary_attribute_value.deserialize_aws_json_1_0(
                data["B"]
            )
        }
    elif "SS" in data:
        import aws_sdk_dynamodb_streams.types.string_set_attribute_value

        return {
            "SS": aws_sdk_dynamodb_streams.types.string_set_attribute_value.deserialize_aws_json_1_0(
                data["SS"]
            )
        }
    elif "NS" in data:
        import aws_sdk_dynamodb_streams.types.number_set_attribute_value

        return {
            "NS": aws_sdk_dynamodb_streams.types.number_set_attribute_value.deserialize_aws_json_1_0(
                data["NS"]
            )
        }
    elif "BS" in data:
        import aws_sdk_dynamodb_streams.types.binary_set_attribute_value

        return {
            "BS": aws_sdk_dynamodb_streams.types.binary_set_attribute_value.deserialize_aws_json_1_0(
                data["BS"]
            )
        }
    elif "M" in data:
        import aws_sdk_dynamodb_streams.types.map_attribute_value

        return {
            "M": aws_sdk_dynamodb_streams.types.map_attribute_value.deserialize_aws_json_1_0(
                data["M"]
            )
        }
    elif "L" in data:
        import aws_sdk_dynamodb_streams.types.list_attribute_value

        return {
            "L": aws_sdk_dynamodb_streams.types.list_attribute_value.deserialize_aws_json_1_0(
                data["L"]
            )
        }
    elif "NULL" in data:
        return {"NULL": data["NULL"]}
    elif "BOOL" in data:
        return {"BOOL": data["BOOL"]}
    else:
        raise DeserializationError("AttributeValue: no recognized variant key")
