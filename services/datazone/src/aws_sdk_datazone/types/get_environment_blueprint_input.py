"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentBlueprintInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id


class GetEnvironmentBlueprintInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the domain in which this blueprint exists.</p>"""
    identifier: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The ID of this Amazon DataZone blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentBlueprintInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentBlueprintInput:
    out: GetEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
    return out
