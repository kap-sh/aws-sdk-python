"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.group_type
    import aws_sdk_iottwinmaker.types.property_names


class PropertyGroupRequest(TypedDict, closed=True):
    group_type: NotRequired["aws_sdk_iottwinmaker.types.group_type.GroupType"]
    """<p>The group type.</p>"""
    property_names: NotRequired[
        "aws_sdk_iottwinmaker.types.property_names.PropertyNames"
    ]
    """<p>The names of properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyGroupRequest) -> dict:
    out: dict = {}
    if "group_type" in value:
        out["groupType"] = value["group_type"]
    if "property_names" in value:
        import aws_sdk_iottwinmaker.types.property_names

        out["propertyNames"] = aws_sdk_iottwinmaker.types.property_names.serialize_json(
            value["property_names"]
        )
    return out


def deserialize_json(data: dict) -> PropertyGroupRequest:
    out: PropertyGroupRequest = {}  # type: ignore[typeddict-item]
    if "groupType" in data:
        out["group_type"] = data["groupType"]
    if "propertyNames" in data:
        import aws_sdk_iottwinmaker.types.property_names

        out["property_names"] = (
            aws_sdk_iottwinmaker.types.property_names.deserialize_json(
                data["propertyNames"]
            )
        )
    return out
