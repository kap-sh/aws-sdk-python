"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentEventDataSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_event_data_summary

DeploymentEventDataSummaryList: TypeAlias = list[
    "aws_sdk_launch_wizard.types.deployment_event_data_summary.DeploymentEventDataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentEventDataSummaryList) -> list:
    import aws_sdk_launch_wizard.types.deployment_event_data_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_launch_wizard.types.deployment_event_data_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeploymentEventDataSummaryList:
    import aws_sdk_launch_wizard.types.deployment_event_data_summary

    out: DeploymentEventDataSummaryList = []
    for item in data:
        out.append(
            aws_sdk_launch_wizard.types.deployment_event_data_summary.deserialize_json(
                item
            )
        )
    return out
