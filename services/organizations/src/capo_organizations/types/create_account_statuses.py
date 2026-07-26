"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.create_account_status

CreateAccountStatuses: TypeAlias = list[
    "capo_organizations.types.create_account_status.CreateAccountStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountStatuses) -> list:
    import capo_organizations.types.create_account_status

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.create_account_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateAccountStatuses:
    import capo_organizations.types.create_account_status

    out: CreateAccountStatuses = []
    for item in data:
        out.append(
            capo_organizations.types.create_account_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
