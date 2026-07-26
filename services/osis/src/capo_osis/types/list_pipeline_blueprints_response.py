"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelineBlueprintsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_blueprints_summary_list


class ListPipelineBlueprintsResponse(TypedDict, closed=True):
    blueprints: NotRequired[
        "capo_osis.types.pipeline_blueprints_summary_list.PipelineBlueprintsSummaryList"
    ]
    """<p>A list of available blueprints for Data Prepper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineBlueprintsResponse) -> dict:
    out: dict = {}
    if "blueprints" in value:
        import capo_osis.types.pipeline_blueprints_summary_list

        out["Blueprints"] = (
            capo_osis.types.pipeline_blueprints_summary_list.serialize_json(
                value["blueprints"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPipelineBlueprintsResponse:
    out: ListPipelineBlueprintsResponse = {}  # type: ignore[typeddict-item]
    if "Blueprints" in data:
        import capo_osis.types.pipeline_blueprints_summary_list

        out["blueprints"] = (
            capo_osis.types.pipeline_blueprints_summary_list.deserialize_json(
                data["Blueprints"]
            )
        )
    return out
