"""Generated from Smithy shape ``com.amazonaws.macie2#DeleteAllowListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class DeleteAllowListRequest(TypedDict):
    id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""
    ignore_job_checks: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>Specifies whether to force deletion of the allow list, even if active classification jobs are configured to use the list.</p> <p>When you try to delete an allow list, Amazon Macie checks for classification jobs that use the list and have a status other than COMPLETE or CANCELLED. By default, Macie rejects your request if any jobs meet these criteria. To skip these checks and delete the list, set this value to true. To delete the list only if no active jobs are configured to use it, set this value to false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAllowListRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAllowListRequest:
    out: DeleteAllowListRequest = {}  # type: ignore[typeddict-item]
    return out
