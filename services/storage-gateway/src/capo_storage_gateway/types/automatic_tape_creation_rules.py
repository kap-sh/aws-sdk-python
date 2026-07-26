"""Generated from Smithy shape ``com.amazonaws.storagegateway#AutomaticTapeCreationRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.automatic_tape_creation_rule

AutomaticTapeCreationRules: TypeAlias = list[
    "capo_storage_gateway.types.automatic_tape_creation_rule.AutomaticTapeCreationRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomaticTapeCreationRules) -> list:
    import capo_storage_gateway.types.automatic_tape_creation_rule

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.automatic_tape_creation_rule.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutomaticTapeCreationRules:
    import capo_storage_gateway.types.automatic_tape_creation_rule

    out: AutomaticTapeCreationRules = []
    for item in data:
        out.append(
            capo_storage_gateway.types.automatic_tape_creation_rule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
