"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

GroupByField: TypeAlias = Literal[
    "activity_name",
    "cloud.account.uid",
    "cloud.provider",
    "cloud.region",
    "compliance.assessments.name",
    "compliance.status",
    "compliance.control",
    "finding_info.title",
    "finding_info.related_events.traits.category",
    "finding_info.types",
    "metadata.product.name",
    "metadata.product.uid",
    "resources.type",
    "resources.uid",
    "severity",
    "status",
    "vulnerabilities.fix_coverage",
    "class_name",
    "vulnerabilities.affected_packages.name",
    "finding_info.analytic.name",
    "compliance.standards",
    "cloud.account.name",
    "vendor_attributes.severity",
    "metadata.product.vendor_name",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "activity_name",
        "cloud.account.uid",
        "cloud.provider",
        "cloud.region",
        "compliance.assessments.name",
        "compliance.status",
        "compliance.control",
        "finding_info.title",
        "finding_info.related_events.traits.category",
        "finding_info.types",
        "metadata.product.name",
        "metadata.product.uid",
        "resources.type",
        "resources.uid",
        "severity",
        "status",
        "vulnerabilities.fix_coverage",
        "class_name",
        "vulnerabilities.affected_packages.name",
        "finding_info.analytic.name",
        "compliance.standards",
        "cloud.account.name",
        "vendor_attributes.severity",
        "metadata.product.vendor_name",
    )
)


def serialize_json(value: GroupByField) -> str:
    return value


def deserialize_json(data: str) -> GroupByField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupByField value: {data!r}")
    return cast(GroupByField, data)
