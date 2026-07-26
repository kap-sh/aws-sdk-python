"""Generated from Smithy shape ``com.amazonaws.glue#DeltaTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.delta_target

DeltaTargetList: TypeAlias = list["capo_glue.types.delta_target.DeltaTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeltaTargetList) -> list:
    import capo_glue.types.delta_target

    out: list = []
    for item in value:
        out.append(capo_glue.types.delta_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeltaTargetList:
    import capo_glue.types.delta_target

    out: DeltaTargetList = []
    for item in data:
        out.append(capo_glue.types.delta_target.deserialize_aws_json_1_1(item))
    return out
