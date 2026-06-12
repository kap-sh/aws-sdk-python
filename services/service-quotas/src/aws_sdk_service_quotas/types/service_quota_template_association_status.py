"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceQuotaTemplateAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

ServiceQuotaTemplateAssociationStatus: TypeAlias = Literal[
    "ASSOCIATED",
    "DISASSOCIATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATED",
        "DISASSOCIATED",
    )
)


def serialize_aws_json_1_1(value: ServiceQuotaTemplateAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceQuotaTemplateAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceQuotaTemplateAssociationStatus value: {data!r}"
        )
    return cast(ServiceQuotaTemplateAssociationStatus, data)
