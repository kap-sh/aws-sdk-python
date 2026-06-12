"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelineBlueprintsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_blueprints_summary_list


class ListPipelineBlueprintsResponse(TypedDict):
    blueprints: NotRequired[
        "aws_sdk_osis.types.pipeline_blueprints_summary_list.PipelineBlueprintsSummaryList"
    ]
    """<p>A list of available blueprints for Data Prepper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineBlueprintsResponse) -> dict:
    out: dict = {}
    if "blueprints" in value:
        import aws_sdk_osis.types.pipeline_blueprints_summary_list

        out["Blueprints"] = (
            aws_sdk_osis.types.pipeline_blueprints_summary_list.serialize_json(
                value["blueprints"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPipelineBlueprintsResponse:
    out: ListPipelineBlueprintsResponse = {}  # type: ignore[typeddict-item]
    if "Blueprints" in data:
        import aws_sdk_osis.types.pipeline_blueprints_summary_list

        out["blueprints"] = (
            aws_sdk_osis.types.pipeline_blueprints_summary_list.deserialize_json(
                data["Blueprints"]
            )
        )
    return out
