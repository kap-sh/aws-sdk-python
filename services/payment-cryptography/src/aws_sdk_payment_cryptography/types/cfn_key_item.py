"""Generated from Smithy shape ``com.amazonaws.magnus.controlplane#CfnKeyItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.resource_policy


class CfnKeyItem(TypedDict):
    policy: NotRequired[
        "aws_sdk_payment_cryptography.types.resource_policy.ResourcePolicy"
    ]
    """The resource-based policy attached to the key, in JSON format."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CfnKeyItem) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CfnKeyItem:
    out: CfnKeyItem = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
