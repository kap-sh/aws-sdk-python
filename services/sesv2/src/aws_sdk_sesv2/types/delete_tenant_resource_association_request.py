"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteTenantResourceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.tenant_name


class DeleteTenantResourceAssociationRequest(TypedDict, closed=True):
    tenant_name: "aws_sdk_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to remove the resource association from.</p>"""
    resource_arn: "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource to remove from the tenant association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTenantResourceAssociationRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DeleteTenantResourceAssociationRequest:
    out: DeleteTenantResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    else:
        raise DeserializationError(
            "DeleteTenantResourceAssociationRequest.tenant_name required"
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "DeleteTenantResourceAssociationRequest.resource_arn required"
        )
    return out
