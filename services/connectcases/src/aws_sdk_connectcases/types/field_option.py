"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_option_name
    import aws_sdk_connectcases.types.field_option_value


class FieldOption(TypedDict, closed=True):
    name: "aws_sdk_connectcases.types.field_option_name.FieldOptionName"
    """<p> <code>FieldOptionName</code> has max length 100 and disallows trailing spaces.</p>"""
    value: "aws_sdk_connectcases.types.field_option_value.FieldOptionValue"
    """<p> <code>FieldOptionValue</code> has max length 100 and must be alphanumeric with hyphens and underscores.</p>"""
    active: "bool"
    """<p>Describes whether the <code>FieldOption</code> is active (displayed) or inactive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldOption) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    out["active"] = value["active"]
    return out


def deserialize_json(data: dict) -> FieldOption:
    out: FieldOption = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FieldOption.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("FieldOption.value required")
    if "active" in data:
        out["active"] = data["active"]
    else:
        raise DeserializationError("FieldOption.active required")
    return out
