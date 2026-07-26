"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfApplicationPolicyStatement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.application_policy_statement

__listOfApplicationPolicyStatement: TypeAlias = list[
    "capo_serverlessapplicationrepository.types.application_policy_statement.ApplicationPolicyStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfApplicationPolicyStatement) -> list:
    import capo_serverlessapplicationrepository.types.application_policy_statement

    out: list = []
    for item in value:
        out.append(
            capo_serverlessapplicationrepository.types.application_policy_statement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfApplicationPolicyStatement:
    import capo_serverlessapplicationrepository.types.application_policy_statement

    out: __listOfApplicationPolicyStatement = []
    for item in data:
        out.append(
            capo_serverlessapplicationrepository.types.application_policy_statement.deserialize_json(
                item
            )
        )
    return out
