"""Generated from Smithy shape ``com.amazonaws.personalize#Schemas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.dataset_schema_summary

Schemas: TypeAlias = list[
    "aws_sdk_personalize.types.dataset_schema_summary.DatasetSchemaSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Schemas) -> list:
    import aws_sdk_personalize.types.dataset_schema_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.dataset_schema_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Schemas:
    import aws_sdk_personalize.types.dataset_schema_summary

    out: Schemas = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.dataset_schema_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
