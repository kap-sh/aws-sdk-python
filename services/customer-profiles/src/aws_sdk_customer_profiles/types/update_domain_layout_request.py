"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateDomainLayoutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.boolean
    import aws_sdk_customer_profiles.types.display_name
    import aws_sdk_customer_profiles.types.layout_type
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.sensitive_string1_to2000000
    import aws_sdk_customer_profiles.types.sensitive_text


class UpdateDomainLayoutRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    layout_definition_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the layout</p>"""
    display_name: NotRequired[
        "aws_sdk_customer_profiles.types.display_name.displayName"
    ]
    """<p>The display name of the layout</p>"""
    is_default: "aws_sdk_customer_profiles.types.boolean.boolean"
    """<p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>"""
    layout_type: NotRequired["aws_sdk_customer_profiles.types.layout_type.LayoutType"]
    """<p>The type of layout that can be used to view data under a Customer Profiles domain.</p>"""
    layout: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000"
    ]
    """<p>A customizable layout that can be used to view data under a Customer Profiles domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainLayoutRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    out["IsDefault"] = value.get("is_default", False)
    if "layout_type" in value:
        import aws_sdk_customer_profiles.types.layout_type

        out["LayoutType"] = aws_sdk_customer_profiles.types.layout_type.serialize_json(
            value["layout_type"]
        )
    if "layout" in value:
        out["Layout"] = value["layout"]
    return out


def deserialize_json(data: dict) -> UpdateDomainLayoutRequest:
    out: UpdateDomainLayoutRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
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
    if "Layout" in data:
        out["layout"] = data["Layout"]
    return out
