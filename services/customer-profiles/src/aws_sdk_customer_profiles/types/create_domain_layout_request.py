"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateDomainLayoutRequest``."""

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
    import aws_sdk_customer_profiles.types.tag_map


class CreateDomainLayoutRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
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
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainLayoutRequest) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    out["DisplayName"] = value["display_name"]
    out["IsDefault"] = value.get("is_default", False)
    import aws_sdk_customer_profiles.types.layout_type

    out["LayoutType"] = aws_sdk_customer_profiles.types.layout_type.serialize_json(
        value["layout_type"]
    )
    out["Layout"] = value["layout"]
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDomainLayoutRequest:
    out: CreateDomainLayoutRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateDomainLayoutRequest.description required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("CreateDomainLayoutRequest.display_name required")
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
        raise DeserializationError("CreateDomainLayoutRequest.layout_type required")
    if "Layout" in data:
        out["layout"] = data["Layout"]
    else:
        raise DeserializationError("CreateDomainLayoutRequest.layout required")
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
