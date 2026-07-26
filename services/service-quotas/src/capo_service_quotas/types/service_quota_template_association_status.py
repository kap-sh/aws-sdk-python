"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceQuotaTemplateAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ServiceQuotaTemplateAssociationStatus: TypeAlias = Literal[
    "ASSOCIATED",
    "DISASSOCIATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuotaTemplateAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceQuotaTemplateAssociationStatus:
    return cast(ServiceQuotaTemplateAssociationStatus, data)
