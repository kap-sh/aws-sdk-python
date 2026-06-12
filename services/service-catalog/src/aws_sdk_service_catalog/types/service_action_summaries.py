"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.service_action_summary

ServiceActionSummaries: TypeAlias = list[
    "aws_sdk_service_catalog.types.service_action_summary.ServiceActionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionSummaries) -> list:
    import aws_sdk_service_catalog.types.service_action_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.service_action_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceActionSummaries:
    import aws_sdk_service_catalog.types.service_action_summary

    out: ServiceActionSummaries = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.service_action_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
