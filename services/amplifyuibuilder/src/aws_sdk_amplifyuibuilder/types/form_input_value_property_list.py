"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormInputValuePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_input_value_property

FormInputValuePropertyList: TypeAlias = list[
    "aws_sdk_amplifyuibuilder.types.form_input_value_property.FormInputValueProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: FormInputValuePropertyList) -> list:
    import aws_sdk_amplifyuibuilder.types.form_input_value_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifyuibuilder.types.form_input_value_property.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FormInputValuePropertyList:
    import aws_sdk_amplifyuibuilder.types.form_input_value_property

    out: FormInputValuePropertyList = []
    for item in data:
        out.append(
            aws_sdk_amplifyuibuilder.types.form_input_value_property.deserialize_json(
                item
            )
        )
    return out
