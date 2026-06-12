"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.impersonation_role

ImpersonationRoleList: TypeAlias = list[
    "aws_sdk_workmail.types.impersonation_role.ImpersonationRole"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRoleList) -> list:
    import aws_sdk_workmail.types.impersonation_role

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.impersonation_role.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImpersonationRoleList:
    import aws_sdk_workmail.types.impersonation_role

    out: ImpersonationRoleList = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.impersonation_role.deserialize_aws_json_1_1(item)
        )
    return out
