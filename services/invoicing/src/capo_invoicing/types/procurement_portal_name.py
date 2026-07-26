"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalName``."""

from typing import Literal, TypeAlias, cast

ProcurementPortalName: TypeAlias = Literal[
    "SAP_BUSINESS_NETWORK",
    "COUPA",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProcurementPortalName:
    return cast(ProcurementPortalName, data)
