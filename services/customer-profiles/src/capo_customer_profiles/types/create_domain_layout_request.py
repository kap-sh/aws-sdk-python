"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateDomainLayoutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.layout_type
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.sensitive_string1_to2000000
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map


class CreateDomainLayoutRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    layout_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""
    description: "capo_customer_profiles.types.sensitive_text.sensitiveText"
    """<p>The description of the layout</p>"""
    display_name: "capo_customer_profiles.types.display_name.displayName"
    """<p>The display name of the layout</p>"""
    is_default: "capo_customer_profiles.types.boolean.boolean"
    """<p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>"""
    layout_type: "capo_customer_profiles.types.layout_type.LayoutType"
    """<p>The type of layout that can be used to view data under a Customer Profiles domain.</p>"""
    layout: "capo_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000"
    """<p>A customizable layout that can be used to view data under a Customer Profiles domain.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainLayoutRequest) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    out["DisplayName"] = value["display_name"]
    out["IsDefault"] = value.get("is_default", False)
    import capo_customer_profiles.types.layout_type

    out["LayoutType"] = capo_customer_profiles.types.layout_type.serialize_json(
        value["layout_type"]
    )
    out["Layout"] = value["layout"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
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
        import capo_customer_profiles.types.layout_type

        out["layout_type"] = capo_customer_profiles.types.layout_type.deserialize_json(
            data["LayoutType"]
        )
    else:
        raise DeserializationError("CreateDomainLayoutRequest.layout_type required")
    if "Layout" in data:
        out["layout"] = data["Layout"]
    else:
        raise DeserializationError("CreateDomainLayoutRequest.layout required")
    if "Tags" in data:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
