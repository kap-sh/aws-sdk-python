"""Generated from Smithy shape ``com.amazonaws.devopsguru#AccountHealths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.account_health

AccountHealths: TypeAlias = list[
    "aws_sdk_devops_guru.types.account_health.AccountHealth"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountHealths) -> list:
    import aws_sdk_devops_guru.types.account_health

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.account_health.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountHealths:
    import aws_sdk_devops_guru.types.account_health

    out: AccountHealths = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.account_health.deserialize_json(item))
    return out
