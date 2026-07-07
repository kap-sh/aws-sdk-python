"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociatedGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.gateway_identifier
    import aws_sdk_direct_connect.types.gateway_type
    import aws_sdk_direct_connect.types.owner_account
    import aws_sdk_direct_connect.types.region


class AssociatedGateway(TypedDict, closed=True):
    id: NotRequired["aws_sdk_direct_connect.types.gateway_identifier.GatewayIdentifier"]
    """<p>The ID of the associated gateway.</p>"""
    type: NotRequired["aws_sdk_direct_connect.types.gateway_type.GatewayType"]
    """<p>The type of associated gateway.</p>"""
    owner_account: NotRequired[
        "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the associated virtual private gateway or transit gateway.</p>"""
    region: NotRequired["aws_sdk_direct_connect.types.region.Region"]
    """<p>The Region where the associated gateway is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedGateway) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import aws_sdk_direct_connect.types.gateway_type

        out["type"] = aws_sdk_direct_connect.types.gateway_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatedGateway:
    out: AssociatedGateway = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import aws_sdk_direct_connect.types.gateway_type

        out["type"] = (
            aws_sdk_direct_connect.types.gateway_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "region" in data:
        out["region"] = data["region"]
    return out
