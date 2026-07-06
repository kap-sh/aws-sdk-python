"""Generated from Smithy shape ``com.amazonaws.customerprofiles#LayoutItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.boolean
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.layout_type
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp


class LayoutItem(TypedDict, closed=True):
    layout_definition_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""
    description: "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    """<p>The description of the layout</p>"""
    display_name: "aws_sdk_customer_profiles.types.display_name.displayName"
    """<p>The display name of the layout</p>"""
    is_default: "aws_sdk_customer_profiles.types.boolean.boolean"
    """<p>If set to true for a layout, this layout will be used by default to view data. If set to false, then layout will not be used by default but it can be used to view data by explicit selection on UI.</p>"""
    layout_type: "aws_sdk_customer_profiles.types.layout_type.LayoutType"
    """<p>The type of layout that can be used to view data under customer profiles domain.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    created_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the layout was created.</p>"""
    last_updated_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the layout was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayoutItem) -> dict:
    out: dict = {}
    out["LayoutDefinitionName"] = value["layout_definition_name"]
    out["Description"] = value["description"]
    out["DisplayName"] = value["display_name"]
    out["IsDefault"] = value.get("is_default", False)
    import aws_sdk_customer_profiles.types.layout_type

    out["LayoutType"] = aws_sdk_customer_profiles.types.layout_type.serialize_json(
        value["layout_type"]
    )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    import aws_sdk_customer_profiles.types.timestamp

    out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> LayoutItem:
    out: LayoutItem = {}  # type: ignore[typeddict-item]
    if "LayoutDefinitionName" in data:
        out["layout_definition_name"] = data["LayoutDefinitionName"]
    else:
        raise DeserializationError("LayoutItem.layout_definition_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("LayoutItem.description required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("LayoutItem.display_name required")
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if "LayoutType" in data:
        import aws_sdk_customer_profiles.types.layout_type

        out["layout_type"] = (
            aws_sdk_customer_profiles.types.layout_type.deserialize_json(
                data["LayoutType"]
            )
        )
    else:
        raise DeserializationError("LayoutItem.layout_type required")
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("LayoutItem.created_at required")
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("LayoutItem.last_updated_at required")
    return out
