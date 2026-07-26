"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSUserAndGroupQuotas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.open_zfs_user_or_group_quota

OpenZFSUserAndGroupQuotas: TypeAlias = list[
    "capo_fsx.types.open_zfs_user_or_group_quota.OpenZFSUserOrGroupQuota"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSUserAndGroupQuotas) -> list:
    import capo_fsx.types.open_zfs_user_or_group_quota

    out: list = []
    for item in value:
        out.append(
            capo_fsx.types.open_zfs_user_or_group_quota.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OpenZFSUserAndGroupQuotas:
    import capo_fsx.types.open_zfs_user_or_group_quota

    out: OpenZFSUserAndGroupQuotas = []
    for item in data:
        out.append(
            capo_fsx.types.open_zfs_user_or_group_quota.deserialize_aws_json_1_1(item)
        )
    return out
