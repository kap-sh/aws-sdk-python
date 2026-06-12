"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_list


class FieldGroup(TypedDict):
    name: NotRequired["str"]
    """<p>Name of the field group.</p>"""
    fields: "aws_sdk_connectcases.types.field_list.FieldList"
    """<p>Represents an ordered list containing field related information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_connectcases.types.field_list

    out["fields"] = aws_sdk_connectcases.types.field_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> FieldGroup:
    out: FieldGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "fields" in data:
        import aws_sdk_connectcases.types.field_list

        out["fields"] = aws_sdk_connectcases.types.field_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("FieldGroup.fields required")
    return out
