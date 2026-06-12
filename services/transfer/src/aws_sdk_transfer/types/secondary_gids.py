"""Generated from Smithy shape ``com.amazonaws.transfer#SecondaryGids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.posix_id

SecondaryGids: TypeAlias = list["aws_sdk_transfer.types.posix_id.PosixId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecondaryGids) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecondaryGids:
    return list(data)
