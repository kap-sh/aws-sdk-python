"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalPreferenceStatus``."""

from typing import Literal, TypeAlias, cast

ProcurementPortalPreferenceStatus: TypeAlias = Literal[
    "PENDING_VERIFICATION",
    "TEST_INITIALIZED",
    "TEST_INITIALIZATION_FAILED",
    "TEST_FAILED",
    "ACTIVE",
    "SUSPENDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalPreferenceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProcurementPortalPreferenceStatus:
    return cast(ProcurementPortalPreferenceStatus, data)
