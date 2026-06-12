"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentPropertyGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.group_type
    import aws_sdk_iottwinmaker.types.property_group_update_type
    import aws_sdk_iottwinmaker.types.property_names


class ComponentPropertyGroupRequest(TypedDict):
    group_type: NotRequired["aws_sdk_iottwinmaker.types.group_type.GroupType"]
    """<p>The group type.</p>"""
    property_names: NotRequired[
        "aws_sdk_iottwinmaker.types.property_names.PropertyNames"
    ]
    """<p>The property names.</p>"""
    update_type: NotRequired[
        "aws_sdk_iottwinmaker.types.property_group_update_type.PropertyGroupUpdateType"
    ]
    """<p>The update type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentPropertyGroupRequest) -> dict:
    out: dict = {}
    if "group_type" in value:
        out["groupType"] = value["group_type"]
    if "property_names" in value:
        import aws_sdk_iottwinmaker.types.property_names

        out["propertyNames"] = aws_sdk_iottwinmaker.types.property_names.serialize_json(
            value["property_names"]
        )
    if "update_type" in value:
        out["updateType"] = value["update_type"]
    return out


def deserialize_json(data: dict) -> ComponentPropertyGroupRequest:
    out: ComponentPropertyGroupRequest = {}  # type: ignore[typeddict-item]
    if "groupType" in data:
        out["group_type"] = data["groupType"]
    if "propertyNames" in data:
        import aws_sdk_iottwinmaker.types.property_names

        out["property_names"] = (
            aws_sdk_iottwinmaker.types.property_names.deserialize_json(
                data["propertyNames"]
            )
        )
    if "updateType" in data:
        out["update_type"] = data["updateType"]
    return out
