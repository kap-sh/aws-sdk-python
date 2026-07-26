"""Generated from Smithy shape ``com.amazonaws.licensemanager#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.string

TagKeyList: TypeAlias = list["capo_license_manager.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeyList:
    return list(data)
