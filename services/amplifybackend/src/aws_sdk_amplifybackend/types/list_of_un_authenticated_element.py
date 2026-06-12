"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfUnAuthenticatedElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.un_authenticated_element

ListOfUnAuthenticatedElement: TypeAlias = list[
    "aws_sdk_amplifybackend.types.un_authenticated_element.UnAuthenticatedElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUnAuthenticatedElement) -> list:
    import aws_sdk_amplifybackend.types.un_authenticated_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifybackend.types.un_authenticated_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfUnAuthenticatedElement:
    import aws_sdk_amplifybackend.types.un_authenticated_element

    out: ListOfUnAuthenticatedElement = []
    for item in data:
        out.append(
            aws_sdk_amplifybackend.types.un_authenticated_element.deserialize_json(item)
        )
    return out
