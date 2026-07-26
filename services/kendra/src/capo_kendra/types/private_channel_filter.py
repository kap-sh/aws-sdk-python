"""Generated from Smithy shape ``com.amazonaws.kendra#PrivateChannelFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.string

PrivateChannelFilter: TypeAlias = list["capo_kendra.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateChannelFilter) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PrivateChannelFilter:
    return list(data)
