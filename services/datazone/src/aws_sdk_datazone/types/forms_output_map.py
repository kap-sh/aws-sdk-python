"""Generated from Smithy shape ``com.amazonaws.datazone#FormsOutputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_entry_output
    import aws_sdk_datazone.types.form_name

FormsOutputMap: TypeAlias = dict[
    "aws_sdk_datazone.types.form_name.FormName",
    "aws_sdk_datazone.types.form_entry_output.FormEntryOutput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FormsOutputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_datazone.types.form_entry_output

        out[key] = aws_sdk_datazone.types.form_entry_output.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FormsOutputMap:
    out: FormsOutputMap = {}
    for key, value in data.items():
        import aws_sdk_datazone.types.form_entry_output

        out[key] = aws_sdk_datazone.types.form_entry_output.deserialize_json(value)
    return out
