"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfApplicationPolicyStatement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.application_policy_statement

__listOfApplicationPolicyStatement: TypeAlias = list[
    "aws_sdk_serverlessapplicationrepository.types.application_policy_statement.ApplicationPolicyStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfApplicationPolicyStatement) -> list:
    import aws_sdk_serverlessapplicationrepository.types.application_policy_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.application_policy_statement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfApplicationPolicyStatement:
    import aws_sdk_serverlessapplicationrepository.types.application_policy_statement

    out: __listOfApplicationPolicyStatement = []
    for item in data:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.application_policy_statement.deserialize_json(
                item
            )
        )
    return out
