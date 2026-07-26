"""Generated from Smithy shape ``com.amazonaws.kendra#IssueSubEntity``."""

from typing import Literal, TypeAlias, cast

IssueSubEntity: TypeAlias = Literal[
    "COMMENTS",
    "ATTACHMENTS",
    "WORKLOGS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssueSubEntity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IssueSubEntity:
    return cast(IssueSubEntity, data)
