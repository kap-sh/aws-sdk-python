"""Generated from Smithy shape ``com.amazonaws.ssm#Targets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.target

Targets: TypeAlias = list["capo_ssm.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Targets) -> list:
    import capo_ssm.types.target

    out: list = []
    for item in value:
        out.append(capo_ssm.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Targets:
    import capo_ssm.types.target

    out: Targets = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.target.deserialize_aws_json_1_1(item))
    return out
