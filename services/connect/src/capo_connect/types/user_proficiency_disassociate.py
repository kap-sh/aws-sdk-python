"""Generated from Smithy shape ``com.amazonaws.connect#UserProficiencyDisassociate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute_name
    import capo_connect.types.predefined_attribute_string_value


class UserProficiencyDisassociate(TypedDict, closed=True):
    attribute_name: (
        "capo_connect.types.predefined_attribute_name.PredefinedAttributeName"
    )
    """<p>The name of user's proficiency.</p>"""
    attribute_value: "capo_connect.types.predefined_attribute_string_value.PredefinedAttributeStringValue"
    """<p>The value of user's proficiency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserProficiencyDisassociate) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    out["AttributeValue"] = value["attribute_value"]
    return out


def deserialize_json(data: dict) -> UserProficiencyDisassociate:
    out: UserProficiencyDisassociate = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "UserProficiencyDisassociate.attribute_name required"
        )
    if "AttributeValue" in data:
        out["attribute_value"] = data["AttributeValue"]
    else:
        raise DeserializationError(
            "UserProficiencyDisassociate.attribute_value required"
        )
    return out
