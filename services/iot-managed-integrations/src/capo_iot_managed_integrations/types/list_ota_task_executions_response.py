"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListOtaTaskExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.ota_next_token
    import capo_iot_managed_integrations.types.ota_task_execution_summaries_list_definition


class ListOtaTaskExecutionsResponse(TypedDict, closed=True):
    execution_summaries: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_execution_summaries_list_definition.OtaTaskExecutionSummariesListDefinition"
    ]
    """<p>A list of all of the over-the-air (OTA) task executions.</p>"""
    next_token: NotRequired[
        "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOtaTaskExecutionsResponse) -> dict:
    out: dict = {}
    if "execution_summaries" in value:
        import capo_iot_managed_integrations.types.ota_task_execution_summaries_list_definition

        out["ExecutionSummaries"] = (
            capo_iot_managed_integrations.types.ota_task_execution_summaries_list_definition.serialize_json(
                value["execution_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOtaTaskExecutionsResponse:
    out: ListOtaTaskExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionSummaries" in data:
        import capo_iot_managed_integrations.types.ota_task_execution_summaries_list_definition

        out["execution_summaries"] = (
            capo_iot_managed_integrations.types.ota_task_execution_summaries_list_definition.deserialize_json(
                data["ExecutionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
