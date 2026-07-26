"""Generated from Smithy shape ``com.amazonaws.odb#IamRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.iam_role

IamRoleList: TypeAlias = list["capo_odb.types.iam_role.IamRole"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamRoleList) -> list:
    import capo_odb.types.iam_role

    out: list = []
    for item in value:
        out.append(capo_odb.types.iam_role.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> IamRoleList:
    import capo_odb.types.iam_role

    out: IamRoleList = []
    for item in data:
        out.append(capo_odb.types.iam_role.deserialize_aws_json_1_0(item))
    return out
