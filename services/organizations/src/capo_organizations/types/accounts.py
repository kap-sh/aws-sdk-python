"""Generated from Smithy shape ``com.amazonaws.organizations#Accounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.account

Accounts: TypeAlias = list["capo_organizations.types.account.Account"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Accounts) -> list:
    import capo_organizations.types.account

    out: list = []
    for item in value:
        out.append(capo_organizations.types.account.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Accounts:
    import capo_organizations.types.account

    out: Accounts = []
    for item in data:
        out.append(capo_organizations.types.account.deserialize_aws_json_1_1(item))
    return out
