"""Generated from Smithy shape ``com.amazonaws.acmpca#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm_pca.types.action_type

ActionList: TypeAlias = list["capo_acm_pca.types.action_type.ActionType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionList) -> list:
    import capo_acm_pca.types.action_type

    out: list = []
    for item in value:
        out.append(capo_acm_pca.types.action_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ActionList:
    import capo_acm_pca.types.action_type

    out: ActionList = []
    for item in data:
        out.append(capo_acm_pca.types.action_type.deserialize_aws_json_1_1(item))
    return out
