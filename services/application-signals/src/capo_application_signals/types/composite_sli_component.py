"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CompositeSliComponent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_application_signals.types.operation_name


class _CompositeSliComponent_OperationName(TypedDict, closed=True):
    OperationName: "capo_application_signals.types.operation_name.OperationName"


CompositeSliComponent: TypeAlias = _CompositeSliComponent_OperationName


# --- restJson1 ser/de ---
def serialize_json(value: CompositeSliComponent) -> dict:
    if "OperationName" in value:
        return {"OperationName": value["OperationName"]}
    else:
        raise SerializationError("CompositeSliComponent: no variant present")


def deserialize_json(data: dict) -> CompositeSliComponent:
    if "OperationName" in data:
        return {"OperationName": data["OperationName"]}
    else:
        raise DeserializationError("CompositeSliComponent: no recognized variant key")
