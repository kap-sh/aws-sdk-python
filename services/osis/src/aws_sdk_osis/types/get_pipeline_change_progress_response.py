"""Generated from Smithy shape ``com.amazonaws.osis#GetPipelineChangeProgressResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.change_progress_status_list


class GetPipelineChangeProgressResponse(TypedDict, closed=True):
    change_progress_statuses: NotRequired[
        "aws_sdk_osis.types.change_progress_status_list.ChangeProgressStatusList"
    ]
    """<p>The current status of the change happening on the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPipelineChangeProgressResponse) -> dict:
    out: dict = {}
    if "change_progress_statuses" in value:
        import aws_sdk_osis.types.change_progress_status_list

        out["ChangeProgressStatuses"] = (
            aws_sdk_osis.types.change_progress_status_list.serialize_json(
                value["change_progress_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPipelineChangeProgressResponse:
    out: GetPipelineChangeProgressResponse = {}  # type: ignore[typeddict-item]
    if "ChangeProgressStatuses" in data:
        import aws_sdk_osis.types.change_progress_status_list

        out["change_progress_statuses"] = (
            aws_sdk_osis.types.change_progress_status_list.deserialize_json(
                data["ChangeProgressStatuses"]
            )
        )
    return out
