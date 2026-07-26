"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListOtaTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.ota_next_token
    import capo_iot_managed_integrations.types.ota_task_list_definition


class ListOtaTasksResponse(TypedDict, closed=True):
    tasks: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_list_definition.OtaTaskListDefinition"
    ]
    """<p>A list of all of the over-the-air (OTA) tasks.</p>"""
    next_token: NotRequired[
        "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOtaTasksResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import capo_iot_managed_integrations.types.ota_task_list_definition

        out["Tasks"] = (
            capo_iot_managed_integrations.types.ota_task_list_definition.serialize_json(
                value["tasks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOtaTasksResponse:
    out: ListOtaTasksResponse = {}  # type: ignore[typeddict-item]
    if "Tasks" in data:
        import capo_iot_managed_integrations.types.ota_task_list_definition

        out["tasks"] = (
            capo_iot_managed_integrations.types.ota_task_list_definition.deserialize_json(
                data["Tasks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
