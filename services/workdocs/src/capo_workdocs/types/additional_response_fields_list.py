"""Generated from Smithy shape ``com.amazonaws.workdocs#AdditionalResponseFieldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.additional_response_field_type

AdditionalResponseFieldsList: TypeAlias = list[
    "capo_workdocs.types.additional_response_field_type.AdditionalResponseFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalResponseFieldsList) -> list:
    import capo_workdocs.types.additional_response_field_type

    out: list = []
    for item in value:
        out.append(
            capo_workdocs.types.additional_response_field_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AdditionalResponseFieldsList:
    import capo_workdocs.types.additional_response_field_type

    out: AdditionalResponseFieldsList = []
    for item in data:
        out.append(
            capo_workdocs.types.additional_response_field_type.deserialize_json(item)
        )
    return out
