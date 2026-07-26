"""Generated from Smithy shape ``com.amazonaws.glue#ResetJobBookmarkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.job_bookmark_entry


class ResetJobBookmarkResponse(TypedDict, closed=True):
    job_bookmark_entry: NotRequired[
        "capo_glue.types.job_bookmark_entry.JobBookmarkEntry"
    ]
    """<p>The reset bookmark entry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetJobBookmarkResponse) -> dict:
    out: dict = {}
    if "job_bookmark_entry" in value:
        import capo_glue.types.job_bookmark_entry

        out["JobBookmarkEntry"] = (
            capo_glue.types.job_bookmark_entry.serialize_aws_json_1_1(
                value["job_bookmark_entry"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetJobBookmarkResponse:
    out: ResetJobBookmarkResponse = {}  # type: ignore[typeddict-item]
    if "JobBookmarkEntry" in data:
        import capo_glue.types.job_bookmark_entry

        out["job_bookmark_entry"] = (
            capo_glue.types.job_bookmark_entry.deserialize_aws_json_1_1(
                data["JobBookmarkEntry"]
            )
        )
    return out
