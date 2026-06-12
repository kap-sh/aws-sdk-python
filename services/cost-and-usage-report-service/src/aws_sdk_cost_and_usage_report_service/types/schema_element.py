"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#SchemaElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

"""<p>Whether or not Amazon Web Services includes resource IDs in the report. </p>"""
SchemaElement: TypeAlias = Literal[
    "RESOURCES",
    "SPLIT_COST_ALLOCATION_DATA",
    "MANUAL_DISCOUNT_COMPATIBILITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCES",
        "SPLIT_COST_ALLOCATION_DATA",
        "MANUAL_DISCOUNT_COMPATIBILITY",
    )
)


def serialize_aws_json_1_1(value: SchemaElement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaElement value: {data!r}")
    return cast(SchemaElement, data)
