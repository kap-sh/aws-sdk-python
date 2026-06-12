"""Generated from Smithy shape ``com.amazonaws.healthlake#DefaultProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.string

DefaultProfiles: TypeAlias = list["aws_sdk_healthlake.types.string.String"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DefaultProfiles) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DefaultProfiles:
    return list(data)
