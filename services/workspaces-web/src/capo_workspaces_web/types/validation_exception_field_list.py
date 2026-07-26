"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ValidationExceptionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.validation_exception_field

ValidationExceptionFieldList: TypeAlias = list[
    "capo_workspaces_web.types.validation_exception_field.ValidationExceptionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionFieldList) -> list:
    import capo_workspaces_web.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.validation_exception_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ValidationExceptionFieldList:
    import capo_workspaces_web.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        out.append(
            capo_workspaces_web.types.validation_exception_field.deserialize_json(item)
        )
    return out
