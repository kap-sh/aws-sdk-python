"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfAuthenticatedElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.authenticated_element

ListOfAuthenticatedElement: TypeAlias = list[
    "aws_sdk_amplifybackend.types.authenticated_element.AuthenticatedElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfAuthenticatedElement) -> list:
    import aws_sdk_amplifybackend.types.authenticated_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifybackend.types.authenticated_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfAuthenticatedElement:
    import aws_sdk_amplifybackend.types.authenticated_element

    out: ListOfAuthenticatedElement = []
    for item in data:
        out.append(
            aws_sdk_amplifybackend.types.authenticated_element.deserialize_json(item)
        )
    return out
