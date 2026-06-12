"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfAdminAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.admin_account

__listOfAdminAccount: TypeAlias = list[
    "aws_sdk_macie2.types.admin_account.AdminAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAdminAccount) -> list:
    import aws_sdk_macie2.types.admin_account

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.admin_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAdminAccount:
    import aws_sdk_macie2.types.admin_account

    out: __listOfAdminAccount = []
    for item in data:
        out.append(aws_sdk_macie2.types.admin_account.deserialize_json(item))
    return out
