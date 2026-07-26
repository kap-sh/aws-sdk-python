"""Generated from Smithy shape ``com.amazonaws.osis#PipelineBlueprint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.string


class PipelineBlueprint(TypedDict, closed=True):
    blueprint_name: NotRequired["capo_osis.types.string.String"]
    """<p>The name of the blueprint.</p>"""
    pipeline_configuration_body: NotRequired["capo_osis.types.string.String"]
    """<p>The YAML configuration of the blueprint.</p>"""
    display_name: NotRequired["capo_osis.types.string.String"]
    """<p>The display name of the blueprint.</p>"""
    display_description: NotRequired["capo_osis.types.string.String"]
    """<p>A description of the blueprint.</p>"""
    service: NotRequired["capo_osis.types.string.String"]
    """<p>The name of the service that the blueprint is associated with.</p>"""
    use_case: NotRequired["capo_osis.types.string.String"]
    """<p>The use case that the blueprint relates to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineBlueprint) -> dict:
    out: dict = {}
    if "blueprint_name" in value:
        out["BlueprintName"] = value["blueprint_name"]
    if "pipeline_configuration_body" in value:
        out["PipelineConfigurationBody"] = value["pipeline_configuration_body"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "display_description" in value:
        out["DisplayDescription"] = value["display_description"]
    if "service" in value:
        out["Service"] = value["service"]
    if "use_case" in value:
        out["UseCase"] = value["use_case"]
    return out


def deserialize_json(data: dict) -> PipelineBlueprint:
    out: PipelineBlueprint = {}  # type: ignore[typeddict-item]
    if "BlueprintName" in data:
        out["blueprint_name"] = data["BlueprintName"]
    if "PipelineConfigurationBody" in data:
        out["pipeline_configuration_body"] = data["PipelineConfigurationBody"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "DisplayDescription" in data:
        out["display_description"] = data["DisplayDescription"]
    if "Service" in data:
        out["service"] = data["Service"]
    if "UseCase" in data:
        out["use_case"] = data["UseCase"]
    return out
