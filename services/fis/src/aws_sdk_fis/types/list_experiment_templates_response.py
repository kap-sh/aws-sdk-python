"""Generated from Smithy shape ``com.amazonaws.fis#ListExperimentTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_summary_list
    import aws_sdk_fis.types.next_token


class ListExperimentTemplatesResponse(TypedDict):
    experiment_templates: NotRequired[
        "aws_sdk_fis.types.experiment_template_summary_list.ExperimentTemplateSummaryList"
    ]
    """<p>The experiment templates.</p>"""
    next_token: NotRequired["aws_sdk_fis.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentTemplatesResponse) -> dict:
    out: dict = {}
    if "experiment_templates" in value:
        import aws_sdk_fis.types.experiment_template_summary_list

        out["experimentTemplates"] = (
            aws_sdk_fis.types.experiment_template_summary_list.serialize_json(
                value["experiment_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExperimentTemplatesResponse:
    out: ListExperimentTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "experimentTemplates" in data:
        import aws_sdk_fis.types.experiment_template_summary_list

        out["experiment_templates"] = (
            aws_sdk_fis.types.experiment_template_summary_list.deserialize_json(
                data["experimentTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
