"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordMetadataValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.string_value
    import capo_bedrock_agentcore.types.string_value_list


class _MemoryRecordMetadataValue_stringValue(TypedDict, closed=True):
    stringValue: "capo_bedrock_agentcore.types.string_value.StringValue"


class _MemoryRecordMetadataValue_stringListValue(TypedDict, closed=True):
    stringListValue: "capo_bedrock_agentcore.types.string_value_list.StringValueList"


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
        import capo_bedrock_agentcore.types.string_value_list

        return {
            "stringListValue": capo_bedrock_agentcore.types.string_value_list.serialize_json(
                value["stringListValue"]
            )
        }
    elif "numberValue" in value:
        return {"numberValue": value["numberValue"]}
    elif "dateTimeValue" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        return {
            "dateTimeValue": capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["dateTimeValue"]
            )
        }
    else:
        raise SerializationError("MemoryRecordMetadataValue: no variant present")


def deserialize_json(data: dict) -> MemoryRecordMetadataValue:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "stringListValue" in data:
        import capo_bedrock_agentcore.types.string_value_list

        return {
            "stringListValue": capo_bedrock_agentcore.types.string_value_list.deserialize_json(
                data["stringListValue"]
            )
        }
    elif "numberValue" in data:
        return {"numberValue": data["numberValue"]}
    elif "dateTimeValue" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        return {
            "dateTimeValue": capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["dateTimeValue"]
            )
        }
    else:
        raise DeserializationError(
            "MemoryRecordMetadataValue: no recognized variant key"
        )
