"""Generated from Smithy shape ``com.amazonaws.proton#DeploymentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.deployment_summary

DeploymentSummaryList: TypeAlias = list[
    "aws_sdk_proton.types.deployment_summary.DeploymentSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeploymentSummaryList) -> list:
    import aws_sdk_proton.types.deployment_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_proton.types.deployment_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DeploymentSummaryList:
    import aws_sdk_proton.types.deployment_summary

    out: DeploymentSummaryList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.deployment_summary.deserialize_aws_json_1_0(item)
        )
    return out
