"""Generated from Smithy shape ``com.amazonaws.mailmanager#PolicyStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.policy_statement

PolicyStatementList: TypeAlias = list[
    "aws_sdk_mailmanager.types.policy_statement.PolicyStatement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStatementList) -> list:
    import aws_sdk_mailmanager.types.policy_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mailmanager.types.policy_statement.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyStatementList:
    import aws_sdk_mailmanager.types.policy_statement

    out: PolicyStatementList = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.policy_statement.deserialize_aws_json_1_0(item)
        )
    return out
