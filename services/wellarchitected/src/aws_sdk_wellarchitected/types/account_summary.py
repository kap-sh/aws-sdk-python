"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AccountSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.check_status
    import aws_sdk_wellarchitected.types.check_status_count

AccountSummary: TypeAlias = dict[
    "aws_sdk_wellarchitected.types.check_status.CheckStatus",
    "aws_sdk_wellarchitected.types.check_status_count.CheckStatusCount",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AccountSummary) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_wellarchitected.types.check_status

        out[aws_sdk_wellarchitected.types.check_status.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> AccountSummary:
    out: AccountSummary = {}
    for key, value in data.items():
        import aws_sdk_wellarchitected.types.check_status

        out[aws_sdk_wellarchitected.types.check_status.deserialize_json(key)] = value
    return out
