"""Generated from Smithy shape ``com.amazonaws.datazone#FormOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_output

FormOutputList: TypeAlias = list["aws_sdk_datazone.types.form_output.FormOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: FormOutputList) -> list:
    import aws_sdk_datazone.types.form_output

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.form_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> FormOutputList:
    import aws_sdk_datazone.types.form_output

    out: FormOutputList = []
    for item in data:
        out.append(aws_sdk_datazone.types.form_output.deserialize_json(item))
    return out
