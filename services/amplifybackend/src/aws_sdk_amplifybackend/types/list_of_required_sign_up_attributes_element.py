"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfRequiredSignUpAttributesElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.required_sign_up_attributes_element

ListOfRequiredSignUpAttributesElement: TypeAlias = list[
    "aws_sdk_amplifybackend.types.required_sign_up_attributes_element.RequiredSignUpAttributesElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRequiredSignUpAttributesElement) -> list:
    import aws_sdk_amplifybackend.types.required_sign_up_attributes_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifybackend.types.required_sign_up_attributes_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfRequiredSignUpAttributesElement:
    import aws_sdk_amplifybackend.types.required_sign_up_attributes_element

    out: ListOfRequiredSignUpAttributesElement = []
    for item in data:
        out.append(
            aws_sdk_amplifybackend.types.required_sign_up_attributes_element.deserialize_json(
                item
            )
        )
    return out
