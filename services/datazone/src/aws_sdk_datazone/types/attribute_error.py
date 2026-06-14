"""Generated from Smithy shape ``com.amazonaws.datazone#AttributeError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_identifier


class AttributeError(TypedDict):
    attribute_identifier: (
        "aws_sdk_datazone.types.attribute_identifier.AttributeIdentifier"
    )
    """<p>The attribute ID as part of the attribute error.</p>"""
    code: "str"
    """<p>The code generated as part of the attribute error.</p>"""
    message: "str"
    """<p>The message generated as part of the attribute error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeError) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AttributeError:
    out: AttributeError = {}  # type: ignore[typeddict-item]
    if "attributeIdentifier" in data:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        raise DeserializationError("AttributeError.attribute_identifier required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("AttributeError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AttributeError.message required")
    return out
