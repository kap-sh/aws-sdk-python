"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteEnvironmentBlueprintConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id


class DeleteEnvironmentBlueprintConfigurationInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the blueprint configuration is deleted.</p>"""
    environment_blueprint_identifier: (
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The ID of the blueprint the configuration of which is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentBlueprintConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentBlueprintConfigurationInput:
    out: DeleteEnvironmentBlueprintConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
