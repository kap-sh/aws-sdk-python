"""Generated from Smithy shape ``com.amazonaws.amp#CreateAlertManagerDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.alert_manager_definition_status


class CreateAlertManagerDefinitionResponse(TypedDict, closed=True):
    status: (
        "capo_amp.types.alert_manager_definition_status.AlertManagerDefinitionStatus"
    )
    """<p>A structure that displays the current status of the alert manager definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAlertManagerDefinitionResponse) -> dict:
    out: dict = {}
    import capo_amp.types.alert_manager_definition_status

    out["status"] = capo_amp.types.alert_manager_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateAlertManagerDefinitionResponse:
    out: CreateAlertManagerDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_amp.types.alert_manager_definition_status

        out["status"] = capo_amp.types.alert_manager_definition_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "CreateAlertManagerDefinitionResponse.status required"
        )
    return out
