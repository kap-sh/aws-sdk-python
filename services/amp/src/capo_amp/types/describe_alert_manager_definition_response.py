"""Generated from Smithy shape ``com.amazonaws.amp#DescribeAlertManagerDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.alert_manager_definition_description


class DescribeAlertManagerDefinitionResponse(TypedDict, closed=True):
    alert_manager_definition: "capo_amp.types.alert_manager_definition_description.AlertManagerDefinitionDescription"
    """<p>The alert manager definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlertManagerDefinitionResponse) -> dict:
    out: dict = {}
    import capo_amp.types.alert_manager_definition_description

    out["alertManagerDefinition"] = (
        capo_amp.types.alert_manager_definition_description.serialize_json(
            value["alert_manager_definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeAlertManagerDefinitionResponse:
    out: DescribeAlertManagerDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "alertManagerDefinition" in data:
        import capo_amp.types.alert_manager_definition_description

        out["alert_manager_definition"] = (
            capo_amp.types.alert_manager_definition_description.deserialize_json(
                data["alertManagerDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAlertManagerDefinitionResponse.alert_manager_definition required"
        )
    return out
