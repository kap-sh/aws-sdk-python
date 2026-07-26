"""Generated from Smithy shape ``com.amazonaws.storagegateway#AutomaticTapeCreationPolicyInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.automatic_tape_creation_rules
    import capo_storage_gateway.types.gateway_arn


class AutomaticTapeCreationPolicyInfo(TypedDict, closed=True):
    automatic_tape_creation_rules: NotRequired[
        "capo_storage_gateway.types.automatic_tape_creation_rules.AutomaticTapeCreationRules"
    ]
    """<p>An automatic tape creation policy consists of a list of automatic tape creation rules. This returns the rules that determine when and how to automatically create new tapes.</p>"""
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomaticTapeCreationPolicyInfo) -> dict:
    out: dict = {}
    if "automatic_tape_creation_rules" in value:
        import capo_storage_gateway.types.automatic_tape_creation_rules

        out["AutomaticTapeCreationRules"] = (
            capo_storage_gateway.types.automatic_tape_creation_rules.serialize_aws_json_1_1(
                value["automatic_tape_creation_rules"]
            )
        )
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomaticTapeCreationPolicyInfo:
    out: AutomaticTapeCreationPolicyInfo = {}  # type: ignore[typeddict-item]
    if "AutomaticTapeCreationRules" in data:
        import capo_storage_gateway.types.automatic_tape_creation_rules

        out["automatic_tape_creation_rules"] = (
            capo_storage_gateway.types.automatic_tape_creation_rules.deserialize_aws_json_1_1(
                data["AutomaticTapeCreationRules"]
            )
        )
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    return out
