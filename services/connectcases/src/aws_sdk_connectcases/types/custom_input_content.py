"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomInputContent``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_value_list


class CustomInputContent(TypedDict):
    fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList"
    """<p>List of field values for the <code>Custom</code> related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomInputContent) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.field_value_list

    out["fields"] = aws_sdk_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> CustomInputContent:
    out: CustomInputContent = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.field_value_list

        out["fields"] = aws_sdk_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("CustomInputContent.fields required")
    return out
