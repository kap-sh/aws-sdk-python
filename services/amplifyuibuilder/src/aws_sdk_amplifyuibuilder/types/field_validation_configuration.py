"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldValidationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.num_values
    import aws_sdk_amplifyuibuilder.types.str_values


class FieldValidationConfiguration(TypedDict):
    type: "str"
    """<p>The validation to perform on an object type.<code/> </p>"""
    str_values: NotRequired["aws_sdk_amplifyuibuilder.types.str_values.StrValues"]
    """<p>The validation to perform on a string value.</p>"""
    num_values: NotRequired["aws_sdk_amplifyuibuilder.types.num_values.NumValues"]
    """<p>The validation to perform on a number value.</p>"""
    validation_message: NotRequired["str"]
    """<p>The validation message to display.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldValidationConfiguration) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "str_values" in value:
        import aws_sdk_amplifyuibuilder.types.str_values

        out["strValues"] = aws_sdk_amplifyuibuilder.types.str_values.serialize_json(
            value["str_values"]
        )
    if "num_values" in value:
        import aws_sdk_amplifyuibuilder.types.num_values

        out["numValues"] = aws_sdk_amplifyuibuilder.types.num_values.serialize_json(
            value["num_values"]
        )
    if "validation_message" in value:
        out["validationMessage"] = value["validation_message"]
    return out


def deserialize_json(data: dict) -> FieldValidationConfiguration:
    out: FieldValidationConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("FieldValidationConfiguration.type required")
    if "strValues" in data:
        import aws_sdk_amplifyuibuilder.types.str_values

        out["str_values"] = aws_sdk_amplifyuibuilder.types.str_values.deserialize_json(
            data["strValues"]
        )
    if "numValues" in data:
        import aws_sdk_amplifyuibuilder.types.num_values

        out["num_values"] = aws_sdk_amplifyuibuilder.types.num_values.deserialize_json(
            data["numValues"]
        )
    if "validationMessage" in data:
        out["validation_message"] = data["validationMessage"]
    return out
