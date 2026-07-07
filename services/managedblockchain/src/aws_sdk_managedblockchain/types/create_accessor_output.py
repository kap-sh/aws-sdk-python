"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateAccessorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.accessor_billing_token_string
    import aws_sdk_managedblockchain.types.accessor_network_type
    import aws_sdk_managedblockchain.types.resource_id_string


class CreateAccessorOutput(TypedDict, closed=True):
    accessor_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the accessor.</p>"""
    billing_token: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_billing_token_string.AccessorBillingTokenString"
    ]
    """<p>The billing token is a property of the Accessor. Use this token to when making calls to the blockchain network. The billing token is used to track your accessor token for billing requests.</p>"""
    network_type: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_network_type.AccessorNetworkType"
    ]
    """<p>The blockchain network that the accessor token is created for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessorOutput) -> dict:
    out: dict = {}
    if "accessor_id" in value:
        out["AccessorId"] = value["accessor_id"]
    if "billing_token" in value:
        out["BillingToken"] = value["billing_token"]
    if "network_type" in value:
        import aws_sdk_managedblockchain.types.accessor_network_type

        out["NetworkType"] = (
            aws_sdk_managedblockchain.types.accessor_network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAccessorOutput:
    out: CreateAccessorOutput = {}  # type: ignore[typeddict-item]
    if "AccessorId" in data:
        out["accessor_id"] = data["AccessorId"]
    if "BillingToken" in data:
        out["billing_token"] = data["BillingToken"]
    if "NetworkType" in data:
        import aws_sdk_managedblockchain.types.accessor_network_type

        out["network_type"] = (
            aws_sdk_managedblockchain.types.accessor_network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
