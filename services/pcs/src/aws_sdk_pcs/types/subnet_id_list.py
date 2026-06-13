"""Generated from Smithy shape ``com.amazonaws.pcs#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pcs.types.subnet_id

SubnetIdList: TypeAlias = list["aws_sdk_pcs.types.subnet_id.SubnetId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SubnetIdList:
    return list(data)
