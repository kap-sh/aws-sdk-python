"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#AdditionalArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.additional_artifact

AdditionalArtifactList: TypeAlias = list[
    "aws_sdk_cost_and_usage_report_service.types.additional_artifact.AdditionalArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalArtifactList) -> list:
    import aws_sdk_cost_and_usage_report_service.types.additional_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_and_usage_report_service.types.additional_artifact.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdditionalArtifactList:
    import aws_sdk_cost_and_usage_report_service.types.additional_artifact

    out: AdditionalArtifactList = []
    for item in data:
        out.append(
            aws_sdk_cost_and_usage_report_service.types.additional_artifact.deserialize_aws_json_1_1(
                item
            )
        )
    return out
