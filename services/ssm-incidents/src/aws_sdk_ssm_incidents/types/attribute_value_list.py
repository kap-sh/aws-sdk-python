"""Generated from Smithy shape ``com.amazonaws.ssmincidents#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.integer_list
    import aws_sdk_ssm_incidents.types.string_list


class _AttributeValueList_stringValues(TypedDict):
    stringValues: "aws_sdk_ssm_incidents.types.string_list.StringList"


class _AttributeValueList_integerValues(TypedDict):
    integerValues: "aws_sdk_ssm_incidents.types.integer_list.IntegerList"


AttributeValueList: TypeAlias = (
    _AttributeValueList_stringValues | _AttributeValueList_integerValues
)


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValueList) -> dict:
    if "stringValues" in value:
        import aws_sdk_ssm_incidents.types.string_list

        return {
            "stringValues": aws_sdk_ssm_incidents.types.string_list.serialize_json(
                value["stringValues"]
            )
        }
    elif "integerValues" in value:
        import aws_sdk_ssm_incidents.types.integer_list

        return {
            "integerValues": aws_sdk_ssm_incidents.types.integer_list.serialize_json(
                value["integerValues"]
            )
        }
    else:
        raise SerializationError("AttributeValueList: no variant present")


def deserialize_json(data: dict) -> AttributeValueList:
    if "stringValues" in data:
        import aws_sdk_ssm_incidents.types.string_list

        return {
            "stringValues": aws_sdk_ssm_incidents.types.string_list.deserialize_json(
                data["stringValues"]
            )
        }
    elif "integerValues" in data:
        import aws_sdk_ssm_incidents.types.integer_list

        return {
            "integerValues": aws_sdk_ssm_incidents.types.integer_list.deserialize_json(
                data["integerValues"]
            )
        }
    else:
        raise DeserializationError("AttributeValueList: no recognized variant key")
