"""Generated from Smithy shape ``com.amazonaws.signin#PolicyStatements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signin.types.policy_statement

PolicyStatements: TypeAlias = list["capo_signin.types.policy_statement.PolicyStatement"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyStatements) -> list:
    import capo_signin.types.policy_statement

    out: list = []
    for item in value:
        out.append(capo_signin.types.policy_statement.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyStatements:
    import capo_signin.types.policy_statement

    out: PolicyStatements = []
    for item in data:
        out.append(capo_signin.types.policy_statement.deserialize_json(item))
    return out
