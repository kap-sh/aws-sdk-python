"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfUnAuthenticatedElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifybackend.types.un_authenticated_element

ListOfUnAuthenticatedElement: TypeAlias = list[
    "capo_amplifybackend.types.un_authenticated_element.UnAuthenticatedElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUnAuthenticatedElement) -> list:
    import capo_amplifybackend.types.un_authenticated_element

    out: list = []
    for item in value:
        out.append(
            capo_amplifybackend.types.un_authenticated_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfUnAuthenticatedElement:
    import capo_amplifybackend.types.un_authenticated_element

    out: ListOfUnAuthenticatedElement = []
    for item in data:
        out.append(
            capo_amplifybackend.types.un_authenticated_element.deserialize_json(item)
        )
    return out
