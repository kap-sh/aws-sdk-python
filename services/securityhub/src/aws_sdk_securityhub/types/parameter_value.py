"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.double
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.integer_list
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class _ParameterValue_Integer(TypedDict):
    Integer: "aws_sdk_securityhub.types.integer.Integer"


class _ParameterValue_IntegerList(TypedDict):
    IntegerList: "aws_sdk_securityhub.types.integer_list.IntegerList"


class _ParameterValue_Double(TypedDict):
    Double: "aws_sdk_securityhub.types.double.Double"


class _ParameterValue_String(TypedDict):
    String: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"


class _ParameterValue_StringList(TypedDict):
    StringList: "aws_sdk_securityhub.types.string_list.StringList"


class _ParameterValue_Boolean(TypedDict):
    Boolean: "aws_sdk_securityhub.types.boolean.Boolean"


class _ParameterValue_Enum(TypedDict):
    Enum: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"


class _ParameterValue_EnumList(TypedDict):
    EnumList: "aws_sdk_securityhub.types.string_list.StringList"


ParameterValue: TypeAlias = (
    _ParameterValue_Integer
    | _ParameterValue_IntegerList
    | _ParameterValue_Double
    | _ParameterValue_String
    | _ParameterValue_StringList
    | _ParameterValue_Boolean
    | _ParameterValue_Enum
    | _ParameterValue_EnumList
)


# --- restJson1 ser/de ---
def serialize_json(value: ParameterValue) -> dict:
    if "Integer" in value:
        return {"Integer": value["Integer"]}
    elif "IntegerList" in value:
        import aws_sdk_securityhub.types.integer_list

        return {
            "IntegerList": aws_sdk_securityhub.types.integer_list.serialize_json(
                value["IntegerList"]
            )
        }
    elif "Double" in value:
        return {"Double": value["Double"]}
    elif "String" in value:
        return {"String": value["String"]}
    elif "StringList" in value:
        import aws_sdk_securityhub.types.string_list

        return {
            "StringList": aws_sdk_securityhub.types.string_list.serialize_json(
                value["StringList"]
            )
        }
    elif "Boolean" in value:
        return {"Boolean": value["Boolean"]}
    elif "Enum" in value:
        return {"Enum": value["Enum"]}
    elif "EnumList" in value:
        import aws_sdk_securityhub.types.string_list

        return {
            "EnumList": aws_sdk_securityhub.types.string_list.serialize_json(
                value["EnumList"]
            )
        }
    else:
        raise SerializationError("ParameterValue: no variant present")


def deserialize_json(data: dict) -> ParameterValue:
    if "Integer" in data:
        return {"Integer": data["Integer"]}
    elif "IntegerList" in data:
        import aws_sdk_securityhub.types.integer_list

        return {
            "IntegerList": aws_sdk_securityhub.types.integer_list.deserialize_json(
                data["IntegerList"]
            )
        }
    elif "Double" in data:
        return {"Double": data["Double"]}
    elif "String" in data:
        return {"String": data["String"]}
    elif "StringList" in data:
        import aws_sdk_securityhub.types.string_list

        return {
            "StringList": aws_sdk_securityhub.types.string_list.deserialize_json(
                data["StringList"]
            )
        }
    elif "Boolean" in data:
        return {"Boolean": data["Boolean"]}
    elif "Enum" in data:
        return {"Enum": data["Enum"]}
    elif "EnumList" in data:
        import aws_sdk_securityhub.types.string_list

        return {
            "EnumList": aws_sdk_securityhub.types.string_list.deserialize_json(
                data["EnumList"]
            )
        }
    else:
        raise DeserializationError("ParameterValue: no recognized variant key")
