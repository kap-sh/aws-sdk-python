"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean_configuration_options
    import aws_sdk_securityhub.types.double_configuration_options
    import aws_sdk_securityhub.types.enum_configuration_options
    import aws_sdk_securityhub.types.enum_list_configuration_options
    import aws_sdk_securityhub.types.integer_configuration_options
    import aws_sdk_securityhub.types.integer_list_configuration_options
    import aws_sdk_securityhub.types.string_configuration_options
    import aws_sdk_securityhub.types.string_list_configuration_options


class _ConfigurationOptions_Integer(TypedDict, closed=True):
    Integer: "aws_sdk_securityhub.types.integer_configuration_options.IntegerConfigurationOptions"


class _ConfigurationOptions_IntegerList(TypedDict, closed=True):
    IntegerList: "aws_sdk_securityhub.types.integer_list_configuration_options.IntegerListConfigurationOptions"


class _ConfigurationOptions_Double(TypedDict, closed=True):
    Double: "aws_sdk_securityhub.types.double_configuration_options.DoubleConfigurationOptions"


class _ConfigurationOptions_String(TypedDict, closed=True):
    String: "aws_sdk_securityhub.types.string_configuration_options.StringConfigurationOptions"


class _ConfigurationOptions_StringList(TypedDict, closed=True):
    StringList: "aws_sdk_securityhub.types.string_list_configuration_options.StringListConfigurationOptions"


class _ConfigurationOptions_Boolean(TypedDict, closed=True):
    Boolean: "aws_sdk_securityhub.types.boolean_configuration_options.BooleanConfigurationOptions"


class _ConfigurationOptions_Enum(TypedDict, closed=True):
    Enum: (
        "aws_sdk_securityhub.types.enum_configuration_options.EnumConfigurationOptions"
    )


class _ConfigurationOptions_EnumList(TypedDict, closed=True):
    EnumList: "aws_sdk_securityhub.types.enum_list_configuration_options.EnumListConfigurationOptions"


ConfigurationOptions: TypeAlias = (
    _ConfigurationOptions_Integer
    | _ConfigurationOptions_IntegerList
    | _ConfigurationOptions_Double
    | _ConfigurationOptions_String
    | _ConfigurationOptions_StringList
    | _ConfigurationOptions_Boolean
    | _ConfigurationOptions_Enum
    | _ConfigurationOptions_EnumList
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationOptions) -> dict:
    if "Integer" in value:
        import aws_sdk_securityhub.types.integer_configuration_options

        return {
            "Integer": aws_sdk_securityhub.types.integer_configuration_options.serialize_json(
                value["Integer"]
            )
        }
    elif "IntegerList" in value:
        import aws_sdk_securityhub.types.integer_list_configuration_options

        return {
            "IntegerList": aws_sdk_securityhub.types.integer_list_configuration_options.serialize_json(
                value["IntegerList"]
            )
        }
    elif "Double" in value:
        import aws_sdk_securityhub.types.double_configuration_options

        return {
            "Double": aws_sdk_securityhub.types.double_configuration_options.serialize_json(
                value["Double"]
            )
        }
    elif "String" in value:
        import aws_sdk_securityhub.types.string_configuration_options

        return {
            "String": aws_sdk_securityhub.types.string_configuration_options.serialize_json(
                value["String"]
            )
        }
    elif "StringList" in value:
        import aws_sdk_securityhub.types.string_list_configuration_options

        return {
            "StringList": aws_sdk_securityhub.types.string_list_configuration_options.serialize_json(
                value["StringList"]
            )
        }
    elif "Boolean" in value:
        import aws_sdk_securityhub.types.boolean_configuration_options

        return {
            "Boolean": aws_sdk_securityhub.types.boolean_configuration_options.serialize_json(
                value["Boolean"]
            )
        }
    elif "Enum" in value:
        import aws_sdk_securityhub.types.enum_configuration_options

        return {
            "Enum": aws_sdk_securityhub.types.enum_configuration_options.serialize_json(
                value["Enum"]
            )
        }
    elif "EnumList" in value:
        import aws_sdk_securityhub.types.enum_list_configuration_options

        return {
            "EnumList": aws_sdk_securityhub.types.enum_list_configuration_options.serialize_json(
                value["EnumList"]
            )
        }
    else:
        raise SerializationError("ConfigurationOptions: no variant present")


def deserialize_json(data: dict) -> ConfigurationOptions:
    if "Integer" in data:
        import aws_sdk_securityhub.types.integer_configuration_options

        return {
            "Integer": aws_sdk_securityhub.types.integer_configuration_options.deserialize_json(
                data["Integer"]
            )
        }
    elif "IntegerList" in data:
        import aws_sdk_securityhub.types.integer_list_configuration_options

        return {
            "IntegerList": aws_sdk_securityhub.types.integer_list_configuration_options.deserialize_json(
                data["IntegerList"]
            )
        }
    elif "Double" in data:
        import aws_sdk_securityhub.types.double_configuration_options

        return {
            "Double": aws_sdk_securityhub.types.double_configuration_options.deserialize_json(
                data["Double"]
            )
        }
    elif "String" in data:
        import aws_sdk_securityhub.types.string_configuration_options

        return {
            "String": aws_sdk_securityhub.types.string_configuration_options.deserialize_json(
                data["String"]
            )
        }
    elif "StringList" in data:
        import aws_sdk_securityhub.types.string_list_configuration_options

        return {
            "StringList": aws_sdk_securityhub.types.string_list_configuration_options.deserialize_json(
                data["StringList"]
            )
        }
    elif "Boolean" in data:
        import aws_sdk_securityhub.types.boolean_configuration_options

        return {
            "Boolean": aws_sdk_securityhub.types.boolean_configuration_options.deserialize_json(
                data["Boolean"]
            )
        }
    elif "Enum" in data:
        import aws_sdk_securityhub.types.enum_configuration_options

        return {
            "Enum": aws_sdk_securityhub.types.enum_configuration_options.deserialize_json(
                data["Enum"]
            )
        }
    elif "EnumList" in data:
        import aws_sdk_securityhub.types.enum_list_configuration_options

        return {
            "EnumList": aws_sdk_securityhub.types.enum_list_configuration_options.deserialize_json(
                data["EnumList"]
            )
        }
    else:
        raise DeserializationError("ConfigurationOptions: no recognized variant key")
