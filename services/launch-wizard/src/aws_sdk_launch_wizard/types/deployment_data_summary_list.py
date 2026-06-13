"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentDataSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_data_summary

DeploymentDataSummaryList: TypeAlias = list[
    "aws_sdk_launch_wizard.types.deployment_data_summary.DeploymentDataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentDataSummaryList) -> list:
    import aws_sdk_launch_wizard.types.deployment_data_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_launch_wizard.types.deployment_data_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeploymentDataSummaryList:
    import aws_sdk_launch_wizard.types.deployment_data_summary

    out: DeploymentDataSummaryList = []
    for item in data:
        out.append(
            aws_sdk_launch_wizard.types.deployment_data_summary.deserialize_json(item)
        )
    return out
