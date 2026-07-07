"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordMetadataValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore.types.string_value
    import aws_sdk_bedrock_agentcore.types.string_value_list


class _MemoryRecordMetadataValue_stringValue(TypedDict, closed=True):
    stringValue: "aws_sdk_bedrock_agentcore.types.string_value.StringValue"


class _MemoryRecordMetadataValue_stringListValue(TypedDict, closed=True):
    stringListValue: "aws_sdk_bedrock_agentcore.types.string_value_list.StringValueList"


class _MemoryRecordMetadataValue_numberValue(TypedDict, closed=True):
    numberValue: "float"


class _MemoryRecordMetadataValue_dateTimeValue(TypedDict, closed=True):
    dateTimeValue: "datetime.datetime"


MemoryRecordMetadataValue: TypeAlias = (
    _MemoryRecordMetadataValue_stringValue
    | _MemoryRecordMetadataValue_stringListValue
    | _MemoryRecordMetadataValue_numberValue
    | _MemoryRecordMetadataValue_dateTimeValue
)


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordMetadataValue) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "stringListValue" in value:
        import aws_sdk_bedrock_agentcore.types.string_value_list

        return {
            "stringListValue": aws_sdk_bedrock_agentcore.types.string_value_list.serialize_json(
                value["stringListValue"]
            )
        }
    elif "numberValue" in value:
        return {"numberValue": value["numberValue"]}
    elif "dateTimeValue" in value:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        return {
            "dateTimeValue": aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["dateTimeValue"]
            )
        }
    else:
        raise SerializationError("MemoryRecordMetadataValue: no variant present")


def deserialize_json(data: dict) -> MemoryRecordMetadataValue:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "stringListValue" in data:
        import aws_sdk_bedrock_agentcore.types.string_value_list

        return {
            "stringListValue": aws_sdk_bedrock_agentcore.types.string_value_list.deserialize_json(
                data["stringListValue"]
            )
        }
    elif "numberValue" in data:
        return {"numberValue": data["numberValue"]}
    elif "dateTimeValue" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        return {
            "dateTimeValue": aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["dateTimeValue"]
            )
        }
    else:
        raise DeserializationError(
            "MemoryRecordMetadataValue: no recognized variant key"
        )
