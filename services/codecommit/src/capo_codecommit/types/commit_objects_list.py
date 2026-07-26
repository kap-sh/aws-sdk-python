"""Generated from Smithy shape ``com.amazonaws.codecommit#CommitObjectsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.commit

CommitObjectsList: TypeAlias = list["capo_codecommit.types.commit.Commit"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommitObjectsList) -> list:
    import capo_codecommit.types.commit

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.commit.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommitObjectsList:
    import capo_codecommit.types.commit

    out: CommitObjectsList = []
    for item in data:
        out.append(capo_codecommit.types.commit.deserialize_aws_json_1_1(item))
    return out
