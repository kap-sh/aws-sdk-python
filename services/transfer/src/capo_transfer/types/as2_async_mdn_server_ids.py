"""Generated from Smithy shape ``com.amazonaws.transfer#As2AsyncMdnServerIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.server_id

As2AsyncMdnServerIds: TypeAlias = list["capo_transfer.types.server_id.ServerId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: As2AsyncMdnServerIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> As2AsyncMdnServerIds:
    return list(data)
