"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRoleIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role_id

ImpersonationRoleIdList: TypeAlias = list[
    "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRoleIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ImpersonationRoleIdList:
    return list(data)
