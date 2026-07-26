"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StepInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhuborchestrator.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.string_map
    import capo_migrationhuborchestrator.types.string_value


class _StepInput_integerValue(TypedDict, closed=True):
    integerValue: "int"


class _StepInput_stringValue(TypedDict, closed=True):
    stringValue: "capo_migrationhuborchestrator.types.string_value.StringValue"


class _StepInput_listOfStringsValue(TypedDict, closed=True):
    listOfStringsValue: "capo_migrationhuborchestrator.types.string_list.StringList"


class _StepInput_mapOfStringValue(TypedDict, closed=True):
    mapOfStringValue: "capo_migrationhuborchestrator.types.string_map.StringMap"


StepInput: TypeAlias = (
    _StepInput_integerValue
    | _StepInput_stringValue
    | _StepInput_listOfStringsValue
    | _StepInput_mapOfStringValue
)


# --- restJson1 ser/de ---
def serialize_json(value: StepInput) -> dict:
    if "integerValue" in value:
        return {"integerValue": value["integerValue"]}
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "listOfStringsValue" in value:
        import capo_migrationhuborchestrator.types.string_list

        return {
            "listOfStringsValue": capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["listOfStringsValue"]
            )
        }
    elif "mapOfStringValue" in value:
        import capo_migrationhuborchestrator.types.string_map

        return {
            "mapOfStringValue": capo_migrationhuborchestrator.types.string_map.serialize_json(
                value["mapOfStringValue"]
            )
        }
    else:
        raise SerializationError("StepInput: no variant present")


def deserialize_json(data: dict) -> StepInput:
    if "integerValue" in data:
        return {"integerValue": data["integerValue"]}
    elif "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "listOfStringsValue" in data:
        import capo_migrationhuborchestrator.types.string_list

        return {
            "listOfStringsValue": capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["listOfStringsValue"]
            )
        }
    elif "mapOfStringValue" in data:
        import capo_migrationhuborchestrator.types.string_map

        return {
            "mapOfStringValue": capo_migrationhuborchestrator.types.string_map.deserialize_json(
                data["mapOfStringValue"]
            )
        }
    else:
        raise DeserializationError("StepInput: no recognized variant key")
