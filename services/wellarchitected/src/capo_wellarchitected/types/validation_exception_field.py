"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.exception_message
    import capo_wellarchitected.types.validation_exception_field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: NotRequired[
        "capo_wellarchitected.types.validation_exception_field_name.ValidationExceptionFieldName"
    ]
    message: NotRequired[
        "capo_wellarchitected.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
