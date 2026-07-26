"""Generated from Smithy shape ``com.amazonaws.workmail#GroupIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.group_identifier

GroupIdentifiers: TypeAlias = list[
    "capo_workmail.types.group_identifier.GroupIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupIdentifiers) -> list:
    import capo_workmail.types.group_identifier

    out: list = []
    for item in value:
        out.append(capo_workmail.types.group_identifier.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GroupIdentifiers:
    import capo_workmail.types.group_identifier

    out: GroupIdentifiers = []
    for item in data:
        out.append(capo_workmail.types.group_identifier.deserialize_aws_json_1_1(item))
    return out
