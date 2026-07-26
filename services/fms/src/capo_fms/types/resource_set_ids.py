"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.base62_id

ResourceSetIds: TypeAlias = list["capo_fms.types.base62_id.Base62Id"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSetIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceSetIds:
    return list(data)
