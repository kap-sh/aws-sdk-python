"""Generated from Smithy shape ``com.amazonaws.datazone#CustomParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description


class CustomParameter(TypedDict):
    key_name: "str"
    """<p>The key name of the parameter.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the parameter.</p>"""
    field_type: "str"
    """<p>The filed type of the parameter.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value of the parameter.</p>"""
    is_editable: NotRequired["bool"]
    """<p>Specifies whether the parameter is editable.</p>"""
    is_optional: NotRequired["bool"]
    """<p>Specifies whether the custom parameter is optional.</p>"""
    is_update_supported: NotRequired["bool"]
    """<p>Specifies whether a parameter value can be updated after creation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomParameter) -> dict:
    out: dict = {}
    out["keyName"] = value["key_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["fieldType"] = value["field_type"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "is_editable" in value:
        out["isEditable"] = value["is_editable"]
    if "is_optional" in value:
        out["isOptional"] = value["is_optional"]
    if "is_update_supported" in value:
        out["isUpdateSupported"] = value["is_update_supported"]
    return out


def deserialize_json(data: dict) -> CustomParameter:
    out: CustomParameter = {}  # type: ignore[typeddict-item]
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    else:
        raise DeserializationError("CustomParameter.key_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "fieldType" in data:
        out["field_type"] = data["fieldType"]
    else:
        raise DeserializationError("CustomParameter.field_type required")
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "isEditable" in data:
        out["is_editable"] = data["isEditable"]
    if "isOptional" in data:
        out["is_optional"] = data["isOptional"]
    if "isUpdateSupported" in data:
        out["is_update_supported"] = data["isUpdateSupported"]
    return out
