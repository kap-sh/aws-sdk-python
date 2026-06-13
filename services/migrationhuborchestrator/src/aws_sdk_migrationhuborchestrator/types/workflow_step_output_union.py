"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepOutputUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_migrationhuborchestrator.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.max_string_list
    import aws_sdk_migrationhuborchestrator.types.max_string_value


class _WorkflowStepOutputUnion_integerValue(TypedDict):
    integerValue: "int"


class _WorkflowStepOutputUnion_stringValue(TypedDict):
    stringValue: (
        "aws_sdk_migrationhuborchestrator.types.max_string_value.MaxStringValue"
    )


class _WorkflowStepOutputUnion_listOfStringValue(TypedDict):
    listOfStringValue: (
        "aws_sdk_migrationhuborchestrator.types.max_string_list.MaxStringList"
    )


WorkflowStepOutputUnion: TypeAlias = (
    _WorkflowStepOutputUnion_integerValue
    | _WorkflowStepOutputUnion_stringValue
    | _WorkflowStepOutputUnion_listOfStringValue
)


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepOutputUnion) -> dict:
    if "integerValue" in value:
        return {"integerValue": value["integerValue"]}
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "listOfStringValue" in value:
        import aws_sdk_migrationhuborchestrator.types.max_string_list

        return {
            "listOfStringValue": aws_sdk_migrationhuborchestrator.types.max_string_list.serialize_json(
                value["listOfStringValue"]
            )
        }
    else:
        raise SerializationError("WorkflowStepOutputUnion: no variant present")


def deserialize_json(data: dict) -> WorkflowStepOutputUnion:
    if "integerValue" in data:
        return {"integerValue": data["integerValue"]}
    elif "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "listOfStringValue" in data:
        import aws_sdk_migrationhuborchestrator.types.max_string_list

        return {
            "listOfStringValue": aws_sdk_migrationhuborchestrator.types.max_string_list.deserialize_json(
                data["listOfStringValue"]
            )
        }
    else:
        raise DeserializationError("WorkflowStepOutputUnion: no recognized variant key")
