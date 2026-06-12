"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadAccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id

WorkloadAccountIds: TypeAlias = list[
    "aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadAccountIds) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadAccountIds:
    return list(data)
