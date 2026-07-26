"""Generated from Smithy shape ``com.amazonaws.kendra#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.subnet_id

SubnetIdList: TypeAlias = list["capo_kendra.types.subnet_id.SubnetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIdList:
    return list(data)
