"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.create_account_state

CreateAccountStates: TypeAlias = list[
    "capo_organizations.types.create_account_state.CreateAccountState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountStates) -> list:
    import capo_organizations.types.create_account_state

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.create_account_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateAccountStates:
    import capo_organizations.types.create_account_state

    out: CreateAccountStates = []
    for item in data:
        out.append(
            capo_organizations.types.create_account_state.deserialize_aws_json_1_1(item)
        )
    return out
