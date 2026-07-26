"""Generated from Smithy shape ``com.amazonaws.evs#EntitlementStatus``."""

from typing import Literal, TypeAlias, cast

EntitlementStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETED",
    "AT_RISK",
    "ENTITLEMENT_REMOVED",
    "CREATE_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntitlementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EntitlementStatus:
    return cast(EntitlementStatus, data)
