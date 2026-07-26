"""Generated from Smithy shape ``com.amazonaws.emr#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.instance

InstanceList: TypeAlias = list["capo_emr.types.instance.Instance"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceList) -> list:
    import capo_emr.types.instance

    out: list = []
    for item in value:
        out.append(capo_emr.types.instance.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceList:
    import capo_emr.types.instance

    out: InstanceList = []
    for item in data:
        out.append(capo_emr.types.instance.deserialize_aws_json_1_1(item))
    return out
