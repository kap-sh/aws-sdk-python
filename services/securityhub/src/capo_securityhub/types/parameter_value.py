"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.double
    import capo_securityhub.types.integer
    import capo_securityhub.types.integer_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class _ParameterValue_Integer(TypedDict, closed=True):
    Integer: "capo_securityhub.types.integer.Integer"


class _ParameterValue_IntegerList(TypedDict, closed=True):
    IntegerList: "capo_securityhub.types.integer_list.IntegerList"


class _ParameterValue_Double(TypedDict, closed=True):
    Double: "capo_securityhub.types.double.Double"


class _ParameterValue_String(TypedDict, closed=True):
    String: "capo_securityhub.types.non_empty_string.NonEmptyString"


class _ParameterValue_StringList(TypedDict, closed=True):
    StringList: "capo_securityhub.types.string_list.StringList"


class _ParameterValue_Boolean(TypedDict, closed=True):
    Boolean: "capo_securityhub.types.boolean.Boolean"


class _ParameterValue_Enum(TypedDict, closed=True):
    Enum: "capo_securityhub.types.non_empty_string.NonEmptyString"


class _ParameterValue_EnumList(TypedDict, closed=True):
    EnumList: "capo_securityhub.types.string_list.StringList"


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
        import capo_securityhub.types.integer_list

        return {
            "IntegerList": capo_securityhub.types.integer_list.serialize_json(
                value["IntegerList"]
            )
        }
    elif "Double" in value:
        return {"Double": value["Double"]}
    elif "String" in value:
        return {"String": value["String"]}
    elif "StringList" in value:
        import capo_securityhub.types.string_list

        return {
            "StringList": capo_securityhub.types.string_list.serialize_json(
                value["StringList"]
            )
        }
    elif "Boolean" in value:
        return {"Boolean": value["Boolean"]}
    elif "Enum" in value:
        return {"Enum": value["Enum"]}
    elif "EnumList" in value:
        import capo_securityhub.types.string_list

        return {
            "EnumList": capo_securityhub.types.string_list.serialize_json(
                value["EnumList"]
            )
        }
    else:
        raise SerializationError("ParameterValue: no variant present")


def deserialize_json(data: dict) -> ParameterValue:
    if "Integer" in data:
        return {"Integer": data["Integer"]}
    elif "IntegerList" in data:
        import capo_securityhub.types.integer_list

        return {
            "IntegerList": capo_securityhub.types.integer_list.deserialize_json(
                data["IntegerList"]
            )
        }
    elif "Double" in data:
        return {"Double": data["Double"]}
    elif "String" in data:
        return {"String": data["String"]}
    elif "StringList" in data:
        import capo_securityhub.types.string_list

        return {
            "StringList": capo_securityhub.types.string_list.deserialize_json(
                data["StringList"]
            )
        }
    elif "Boolean" in data:
        return {"Boolean": data["Boolean"]}
    elif "Enum" in data:
        return {"Enum": data["Enum"]}
    elif "EnumList" in data:
        import capo_securityhub.types.string_list

        return {
            "EnumList": capo_securityhub.types.string_list.deserialize_json(
                data["EnumList"]
            )
        }
    else:
        raise DeserializationError("ParameterValue: no recognized variant key")
