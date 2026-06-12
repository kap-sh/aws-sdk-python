"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateTenantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.tag_list
    import aws_sdk_sesv2.types.tenant_name
    import aws_sdk_sesv2.types.tenant_suppression_attributes


class CreateTenantRequest(TypedDict):
    tenant_name: "aws_sdk_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to create. The name can contain up to 64 alphanumeric characters, including letters, numbers, hyphens (-) and underscores (_) only.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the tenant</p>"""
    suppression_attributes: NotRequired[
        "aws_sdk_sesv2.types.tenant_suppression_attributes.TenantSuppressionAttributes"
    ]
    """<p>An object that contains information about the suppression list preferences for the tenant. Use this to configure tenant-level suppression at creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTenantRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    if "suppression_attributes" in value:
        import aws_sdk_sesv2.types.tenant_suppression_attributes

        out["SuppressionAttributes"] = (
            aws_sdk_sesv2.types.tenant_suppression_attributes.serialize_json(
                value["suppression_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTenantRequest:
    out: CreateTenantRequest = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    else:
        raise DeserializationError("CreateTenantRequest.tenant_name required")
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if "SuppressionAttributes" in data:
        import aws_sdk_sesv2.types.tenant_suppression_attributes

        out["suppression_attributes"] = (
            aws_sdk_sesv2.types.tenant_suppression_attributes.deserialize_json(
                data["SuppressionAttributes"]
            )
        )
    return out
