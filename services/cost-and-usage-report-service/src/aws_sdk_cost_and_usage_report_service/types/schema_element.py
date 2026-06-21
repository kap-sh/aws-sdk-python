"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#SchemaElement``."""

from typing import Literal, TypeAlias, cast

"""<p>Whether or not Amazon Web Services includes resource IDs in the report. </p>"""
SchemaElement: TypeAlias = Literal[
    "RESOURCES",
    "SPLIT_COST_ALLOCATION_DATA",
    "MANUAL_DISCOUNT_COMPATIBILITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaElement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaElement:
    return cast(SchemaElement, data)
