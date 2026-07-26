"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role

ImpersonationRoleList: TypeAlias = list[
    "capo_workmail.types.impersonation_role.ImpersonationRole"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRoleList) -> list:
    import capo_workmail.types.impersonation_role

    out: list = []
    for item in value:
        out.append(capo_workmail.types.impersonation_role.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImpersonationRoleList:
    import capo_workmail.types.impersonation_role

    out: ImpersonationRoleList = []
    for item in data:
        out.append(
            capo_workmail.types.impersonation_role.deserialize_aws_json_1_1(item)
        )
    return out
