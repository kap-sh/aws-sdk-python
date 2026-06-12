"""Generated from Smithy shape ``com.amazonaws.codecommit#CommitObjectsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit

CommitObjectsList: TypeAlias = list["aws_sdk_codecommit.types.commit.Commit"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommitObjectsList) -> list:
    import aws_sdk_codecommit.types.commit

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.commit.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommitObjectsList:
    import aws_sdk_codecommit.types.commit

    out: CommitObjectsList = []
    for item in data:
        out.append(aws_sdk_codecommit.types.commit.deserialize_aws_json_1_1(item))
    return out
