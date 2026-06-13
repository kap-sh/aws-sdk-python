"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector_summary

ActionConnectorSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.action_connector_summary.ActionConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSummaryList) -> list:
    import aws_sdk_quicksight.types.action_connector_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.action_connector_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ActionConnectorSummaryList:
    import aws_sdk_quicksight.types.action_connector_summary

    out: ActionConnectorSummaryList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.action_connector_summary.deserialize_json(item)
        )
    return out
