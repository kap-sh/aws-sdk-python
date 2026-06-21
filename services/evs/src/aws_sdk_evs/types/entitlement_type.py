"""Generated from Smithy shape ``com.amazonaws.evs#EntitlementType``."""

from typing import Literal, TypeAlias, cast

EntitlementType: TypeAlias = Literal["WINDOWS_SERVER",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntitlementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EntitlementType:
    return cast(EntitlementType, data)
