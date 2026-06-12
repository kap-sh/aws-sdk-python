"""Generated from Smithy shape ``com.amazonaws.dax#SubnetGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dax.types.subnet_group

SubnetGroupList: TypeAlias = list["aws_sdk_dax.types.subnet_group.SubnetGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetGroupList) -> list:
    import aws_sdk_dax.types.subnet_group

    out: list = []
    for item in value:
        out.append(aws_sdk_dax.types.subnet_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubnetGroupList:
    import aws_sdk_dax.types.subnet_group

    out: SubnetGroupList = []
    for item in data:
        out.append(aws_sdk_dax.types.subnet_group.deserialize_aws_json_1_1(item))
    return out
