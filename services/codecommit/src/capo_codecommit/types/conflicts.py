"""Generated from Smithy shape ``com.amazonaws.codecommit#Conflicts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.conflict

Conflicts: TypeAlias = list["capo_codecommit.types.conflict.Conflict"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Conflicts) -> list:
    import capo_codecommit.types.conflict

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.conflict.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Conflicts:
    import capo_codecommit.types.conflict

    out: Conflicts = []
    for item in data:
        out.append(capo_codecommit.types.conflict.deserialize_aws_json_1_1(item))
    return out
