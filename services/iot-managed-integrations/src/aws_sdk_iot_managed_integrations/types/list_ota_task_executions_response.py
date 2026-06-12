"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListOtaTaskExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_next_token
    import aws_sdk_iot_managed_integrations.types.ota_task_execution_summaries_list_definition


class ListOtaTaskExecutionsResponse(TypedDict):
    execution_summaries: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_execution_summaries_list_definition.OtaTaskExecutionSummariesListDefinition"
    ]
    """<p>A list of all of the over-the-air (OTA) task executions.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_next_token.OtaNextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOtaTaskExecutionsResponse) -> dict:
    out: dict = {}
    if "execution_summaries" in value:
        import aws_sdk_iot_managed_integrations.types.ota_task_execution_summaries_list_definition

        out["ExecutionSummaries"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_execution_summaries_list_definition.serialize_json(
                value["execution_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOtaTaskExecutionsResponse:
    out: ListOtaTaskExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionSummaries" in data:
        import aws_sdk_iot_managed_integrations.types.ota_task_execution_summaries_list_definition

        out["execution_summaries"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_execution_summaries_list_definition.deserialize_json(
                data["ExecutionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
