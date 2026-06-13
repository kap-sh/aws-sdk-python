"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteEnvironmentBlueprintInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id


class DeleteEnvironmentBlueprintInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the blueprint is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The ID of the blueprint that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentBlueprintInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentBlueprintInput:
    out: DeleteEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
    return out
