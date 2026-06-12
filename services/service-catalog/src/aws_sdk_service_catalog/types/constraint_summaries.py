"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ConstraintSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.constraint_summary

ConstraintSummaries: TypeAlias = list[
    "aws_sdk_service_catalog.types.constraint_summary.ConstraintSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintSummaries) -> list:
    import aws_sdk_service_catalog.types.constraint_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.constraint_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConstraintSummaries:
    import aws_sdk_service_catalog.types.constraint_summary

    out: ConstraintSummaries = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.constraint_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
