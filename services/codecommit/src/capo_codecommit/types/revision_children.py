"""Generated from Smithy shape ``com.amazonaws.codecommit#RevisionChildren``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.revision_id

RevisionChildren: TypeAlias = list["capo_codecommit.types.revision_id.RevisionId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionChildren) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RevisionChildren:
    return list(data)
