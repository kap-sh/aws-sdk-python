"""Generated from Smithy shape ``com.amazonaws.storagegateway#AutomaticTapeCreationPolicyInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.automatic_tape_creation_policy_info

AutomaticTapeCreationPolicyInfos: TypeAlias = list[
    "capo_storage_gateway.types.automatic_tape_creation_policy_info.AutomaticTapeCreationPolicyInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomaticTapeCreationPolicyInfos) -> list:
    import capo_storage_gateway.types.automatic_tape_creation_policy_info

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.automatic_tape_creation_policy_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutomaticTapeCreationPolicyInfos:
    import capo_storage_gateway.types.automatic_tape_creation_policy_info

    out: AutomaticTapeCreationPolicyInfos = []
    for item in data:
        out.append(
            capo_storage_gateway.types.automatic_tape_creation_policy_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
