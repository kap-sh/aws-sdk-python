"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ApprovalStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.approval_status_details

ApprovalStatuses: TypeAlias = dict[
    "aws_sdk_cleanrooms.types.account_id.AccountId",
    "aws_sdk_cleanrooms.types.approval_status_details.ApprovalStatusDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ApprovalStatuses) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_cleanrooms.types.approval_status_details

        out[key] = aws_sdk_cleanrooms.types.approval_status_details.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ApprovalStatuses:
    out: ApprovalStatuses = {}
    for key, value in data.items():
        import aws_sdk_cleanrooms.types.approval_status_details

        out[key] = aws_sdk_cleanrooms.types.approval_status_details.deserialize_json(
            value
        )
    return out
