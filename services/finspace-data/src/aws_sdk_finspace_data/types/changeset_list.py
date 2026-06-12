"""Generated from Smithy shape ``com.amazonaws.finspacedata#ChangesetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.changeset_summary

ChangesetList: TypeAlias = list[
    "aws_sdk_finspace_data.types.changeset_summary.ChangesetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangesetList) -> list:
    import aws_sdk_finspace_data.types.changeset_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace_data.types.changeset_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangesetList:
    import aws_sdk_finspace_data.types.changeset_summary

    out: ChangesetList = []
    for item in data:
        out.append(aws_sdk_finspace_data.types.changeset_summary.deserialize_json(item))
    return out
