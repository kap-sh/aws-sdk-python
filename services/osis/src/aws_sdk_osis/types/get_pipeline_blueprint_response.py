"""Generated from Smithy shape ``com.amazonaws.osis#GetPipelineBlueprintResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_blueprint
    import aws_sdk_osis.types.string


class GetPipelineBlueprintResponse(TypedDict, closed=True):
    blueprint: NotRequired["aws_sdk_osis.types.pipeline_blueprint.PipelineBlueprint"]
    """<p>The requested blueprint in YAML format.</p>"""
    format: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The format of the blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPipelineBlueprintResponse) -> dict:
    out: dict = {}
    if "blueprint" in value:
        import aws_sdk_osis.types.pipeline_blueprint

        out["Blueprint"] = aws_sdk_osis.types.pipeline_blueprint.serialize_json(
            value["blueprint"]
        )
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_json(data: dict) -> GetPipelineBlueprintResponse:
    out: GetPipelineBlueprintResponse = {}  # type: ignore[typeddict-item]
    if "Blueprint" in data:
        import aws_sdk_osis.types.pipeline_blueprint

        out["blueprint"] = aws_sdk_osis.types.pipeline_blueprint.deserialize_json(
            data["Blueprint"]
        )
    if "Format" in data:
        out["format"] = data["Format"]
    return out
