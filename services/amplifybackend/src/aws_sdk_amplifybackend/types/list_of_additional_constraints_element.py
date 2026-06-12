"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfAdditionalConstraintsElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.additional_constraints_element

ListOfAdditionalConstraintsElement: TypeAlias = list[
    "aws_sdk_amplifybackend.types.additional_constraints_element.AdditionalConstraintsElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfAdditionalConstraintsElement) -> list:
    import aws_sdk_amplifybackend.types.additional_constraints_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifybackend.types.additional_constraints_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfAdditionalConstraintsElement:
    import aws_sdk_amplifybackend.types.additional_constraints_element

    out: ListOfAdditionalConstraintsElement = []
    for item in data:
        out.append(
            aws_sdk_amplifybackend.types.additional_constraints_element.deserialize_json(
                item
            )
        )
    return out
