"""Generated from Smithy shape ``com.amazonaws.invoicing#TaxAuthorityStatus``."""

from typing import Literal, TypeAlias, cast

TaxAuthorityStatus: TypeAlias = Literal[
    "ISSUED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxAuthorityStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TaxAuthorityStatus:
    return cast(TaxAuthorityStatus, data)
