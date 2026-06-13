"""Generated from Smithy shape ``com.amazonaws.amp#PutAlertManagerDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.alert_manager_definition_status


class PutAlertManagerDefinitionResponse(TypedDict):
    status: (
        "aws_sdk_amp.types.alert_manager_definition_status.AlertManagerDefinitionStatus"
    )
    """<p>A structure that returns the current status of the alert manager definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAlertManagerDefinitionResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.alert_manager_definition_status

    out["status"] = aws_sdk_amp.types.alert_manager_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> PutAlertManagerDefinitionResponse:
    out: PutAlertManagerDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_amp.types.alert_manager_definition_status

        out["status"] = (
            aws_sdk_amp.types.alert_manager_definition_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("PutAlertManagerDefinitionResponse.status required")
    return out
