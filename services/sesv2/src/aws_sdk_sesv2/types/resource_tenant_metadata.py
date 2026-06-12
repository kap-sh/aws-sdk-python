"""Generated from Smithy shape ``com.amazonaws.sesv2#ResourceTenantMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.tenant_id
    import aws_sdk_sesv2.types.tenant_name
    import aws_sdk_sesv2.types.timestamp


class ResourceTenantMetadata(TypedDict):
    tenant_name: NotRequired["aws_sdk_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant associated with the resource.</p>"""
    tenant_id: NotRequired["aws_sdk_sesv2.types.tenant_id.TenantId"]
    """<p>A unique identifier for the tenant associated with the resource.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    associated_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The date and time when the resource was associated with the tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTenantMetadata) -> dict:
    out: dict = {}
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "associated_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["AssociatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["associated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ResourceTenantMetadata:
    out: ResourceTenantMetadata = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    if "TenantId" in data:
        out["tenant_id"] = data["TenantId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "AssociatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["associated_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["AssociatedTimestamp"]
        )
    return out
