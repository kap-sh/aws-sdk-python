"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetDomainLayoutResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.boolean
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.layout_type
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.sensitive_string1_to2000000
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp


class GetDomainLayoutResponse(TypedDict):
    layout_definition_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""
    description: "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    """<p>The description of the layout</p>"""
    display_name: "aws_sdk_customer_profiles.types.display_name.displayName"
    """<p>The display name of the layout</p>"""
    is_default: "aws_sdk_customer_profiles.types.boolean.boolean"
    """<p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>"""
    layout_type: "aws_sdk_customer_profiles.types.layout_type.LayoutType"
    """<p>The type of layout that can be used to view data under a Customer Profiles domain.</p>"""
    layout: "aws_sdk_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000"
    """<p>A customizable layout that can be used to view data under a Customer Profiles domain.</p>"""
    version: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The version used to create layout.</p>"""
    created_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the layout was created.</p>"""
    last_updated_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the layout was most recently updated.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainLayoutResponse) -> dict:
    out: dict = {}
    out["LayoutDefinitionName"] = value["layout_definition_name"]
    out["Description"] = value["description"]
    out["DisplayName"] = value["display_name"]
    out["IsDefault"] = value.get("is_default", False)
    import aws_sdk_customer_profiles.types.layout_type

    out["LayoutType"] = aws_sdk_customer_profiles.types.layout_type.serialize_json(
        value["layout_type"]
    )
    out["Layout"] = value["layout"]
    out["Version"] = value["version"]
    import aws_sdk_customer_profiles.types.timestamp

    out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetDomainLayoutResponse:
    out: GetDomainLayoutResponse = {}  # type: ignore[typeddict-item]
    if "LayoutDefinitionName" in data:
        out["layout_definition_name"] = data["LayoutDefinitionName"]
    else:
        raise DeserializationError(
            "GetDomainLayoutResponse.layout_definition_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("GetDomainLayoutResponse.description required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("GetDomainLayoutResponse.display_name required")
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
        raise DeserializationError("GetDomainLayoutResponse.layout_type required")
    if "Layout" in data:
        out["layout"] = data["Layout"]
    else:
        raise DeserializationError("GetDomainLayoutResponse.layout required")
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("GetDomainLayoutResponse.version required")
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("GetDomainLayoutResponse.created_at required")
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("GetDomainLayoutResponse.last_updated_at required")
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
