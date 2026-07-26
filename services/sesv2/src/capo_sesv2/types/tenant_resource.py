"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.resource_type


class TenantResource(TypedDict, closed=True):
    resource_type: NotRequired["capo_sesv2.types.resource_type.ResourceType"]
    """<p>The type of resource associated with the tenant. Valid values are <code>EMAIL_IDENTITY</code>, <code>CONFIGURATION_SET</code>, or <code>EMAIL_TEMPLATE</code>.</p>"""
    resource_arn: NotRequired[
        "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource associated with the tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TenantResource) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_sesv2.types.resource_type

        out["ResourceType"] = capo_sesv2.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> TenantResource:
    out: TenantResource = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_sesv2.types.resource_type

        out["resource_type"] = capo_sesv2.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
