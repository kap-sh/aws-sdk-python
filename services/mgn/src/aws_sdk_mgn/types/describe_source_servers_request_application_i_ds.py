"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeSourceServersRequestApplicationIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.application_id

DescribeSourceServersRequestApplicationIDs: TypeAlias = list[
    "aws_sdk_mgn.types.application_id.ApplicationID"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceServersRequestApplicationIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeSourceServersRequestApplicationIDs:
    return list(data)
