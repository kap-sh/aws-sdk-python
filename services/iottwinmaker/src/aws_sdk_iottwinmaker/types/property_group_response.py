"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.group_type
    import aws_sdk_iottwinmaker.types.property_names


class PropertyGroupResponse(TypedDict):
    group_type: "aws_sdk_iottwinmaker.types.group_type.GroupType"
    """<p>The group types.</p>"""
    property_names: "aws_sdk_iottwinmaker.types.property_names.PropertyNames"
    """<p>The names of properties.</p>"""
    is_inherited: "aws_sdk_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property group is inherited from a parent entity</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyGroupResponse) -> dict:
    out: dict = {}
    out["groupType"] = value["group_type"]
    import aws_sdk_iottwinmaker.types.property_names

    out["propertyNames"] = aws_sdk_iottwinmaker.types.property_names.serialize_json(
        value["property_names"]
    )
    out["isInherited"] = value["is_inherited"]
    return out


def deserialize_json(data: dict) -> PropertyGroupResponse:
    out: PropertyGroupResponse = {}  # type: ignore[typeddict-item]
    if "groupType" in data:
        out["group_type"] = data["groupType"]
    else:
        raise DeserializationError("PropertyGroupResponse.group_type required")
    if "propertyNames" in data:
        import aws_sdk_iottwinmaker.types.property_names

        out["property_names"] = (
            aws_sdk_iottwinmaker.types.property_names.deserialize_json(
                data["propertyNames"]
            )
        )
    else:
        raise DeserializationError("PropertyGroupResponse.property_names required")
    if "isInherited" in data:
        out["is_inherited"] = data["isInherited"]
    else:
        raise DeserializationError("PropertyGroupResponse.is_inherited required")
    return out
