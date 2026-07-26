"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentBlueprintConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_blueprint_id


class GetEnvironmentBlueprintConfigurationInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where this blueprint exists.</p>"""
    environment_blueprint_identifier: (
        "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>He ID of the blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentBlueprintConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentBlueprintConfigurationInput:
    out: GetEnvironmentBlueprintConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
