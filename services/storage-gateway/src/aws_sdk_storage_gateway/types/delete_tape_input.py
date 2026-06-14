"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapeInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.tape_arn


class DeleteTapeInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    tape_arn: "aws_sdk_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape to delete.</p>"""
    bypass_governance_retention: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>Set to <code>TRUE</code> to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to <code>governance</code> can be deleted. Archived tapes with tape retention lock set to <code>compliance</code> can't be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapeInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["TapeARN"] = value["tape_arn"]
    out["BypassGovernanceRetention"] = value.get("bypass_governance_retention", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapeInput:
    out: DeleteTapeInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("DeleteTapeInput.gateway_arn required")
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    else:
        raise DeserializationError("DeleteTapeInput.tape_arn required")
    if "BypassGovernanceRetention" in data:
        out["bypass_governance_retention"] = data["BypassGovernanceRetention"]
    else:
        out["bypass_governance_retention"] = False
    return out
