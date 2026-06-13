"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_input

MetadataFormInputs: TypeAlias = list["aws_sdk_datazone.types.form_input.FormInput"]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormInputs) -> list:
    import aws_sdk_datazone.types.form_input

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.form_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataFormInputs:
    import aws_sdk_datazone.types.form_input

    out: MetadataFormInputs = []
    for item in data:
        out.append(aws_sdk_datazone.types.form_input.deserialize_json(item))
    return out
