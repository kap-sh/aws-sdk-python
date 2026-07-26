"""Generated from Smithy shape ``com.amazonaws.resiliencehub#IamRoleArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.iam_role_arn

IamRoleArnList: TypeAlias = list["capo_resiliencehub.types.iam_role_arn.IamRoleArn"]


# --- restJson1 ser/de ---
def serialize_json(value: IamRoleArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> IamRoleArnList:
    return list(data)
