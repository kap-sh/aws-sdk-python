"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataForms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_output

MetadataForms: TypeAlias = list["aws_sdk_datazone.types.form_output.FormOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataForms) -> list:
    import aws_sdk_datazone.types.form_output

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.form_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataForms:
    import aws_sdk_datazone.types.form_output

    out: MetadataForms = []
    for item in data:
        out.append(aws_sdk_datazone.types.form_output.deserialize_json(item))
    return out
