"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.tenant_id
    import capo_sesv2.types.tenant_name
    import capo_sesv2.types.timestamp


class TenantInfo(TypedDict, closed=True):
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant.</p>"""
    tenant_id: NotRequired["capo_sesv2.types.tenant_id.TenantId"]
    """<p>A unique identifier for the tenant.</p>"""
    tenant_arn: NotRequired["capo_sesv2.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the tenant.</p>"""
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The date and time when the tenant was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TenantInfo) -> dict:
    out: dict = {}
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    if "tenant_arn" in value:
        out["TenantArn"] = value["tenant_arn"]
    if "created_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CreatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> TenantInfo:
    out: TenantInfo = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    if "TenantId" in data:
        out["tenant_id"] = data["TenantId"]
    if "TenantArn" in data:
        out["tenant_arn"] = data["TenantArn"]
    if "CreatedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["created_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    return out
