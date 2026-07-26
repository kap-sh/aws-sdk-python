"""Generated from Smithy shape ``com.amazonaws.licensemanager#MaxSize3StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.string

MaxSize3StringList: TypeAlias = list["capo_license_manager.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaxSize3StringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MaxSize3StringList:
    return list(data)
