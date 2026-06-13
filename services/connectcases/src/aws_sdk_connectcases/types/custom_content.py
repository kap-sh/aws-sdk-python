"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomContent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_value_list


class CustomContent(TypedDict):
    fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList"
    """<p>List of field values for the <code>Custom</code> related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomContent) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.field_value_list

    out["fields"] = aws_sdk_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> CustomContent:
    out: CustomContent = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.field_value_list

        out["fields"] = aws_sdk_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("CustomContent.fields required")
    return out
