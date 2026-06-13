"""Generated from Smithy shape ``com.amazonaws.omics#SubmissionSummary``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SubmissionSummary(TypedDict):
    successful_start_submission_count: NotRequired["int"]
    """<p>The number of successful start submissions.</p>"""
    failed_start_submission_count: NotRequired["int"]
    """<p>The number of failed start submissions.</p>"""
    pending_start_submission_count: NotRequired["int"]
    """<p>The number of pending start submissions.</p>"""
    successful_cancel_submission_count: NotRequired["int"]
    """<p>The number of successful cancel submissions.</p>"""
    failed_cancel_submission_count: NotRequired["int"]
    """<p>The number of failed cancel submissions.</p>"""
    successful_delete_submission_count: NotRequired["int"]
    """<p>The number of successful delete submissions.</p>"""
    failed_delete_submission_count: NotRequired["int"]
    """<p>The number of failed delete submissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmissionSummary) -> dict:
    out: dict = {}
    if "successful_start_submission_count" in value:
        out["successfulStartSubmissionCount"] = value[
            "successful_start_submission_count"
        ]
    if "failed_start_submission_count" in value:
        out["failedStartSubmissionCount"] = value["failed_start_submission_count"]
    if "pending_start_submission_count" in value:
        out["pendingStartSubmissionCount"] = value["pending_start_submission_count"]
    if "successful_cancel_submission_count" in value:
        out["successfulCancelSubmissionCount"] = value[
            "successful_cancel_submission_count"
        ]
    if "failed_cancel_submission_count" in value:
        out["failedCancelSubmissionCount"] = value["failed_cancel_submission_count"]
    if "successful_delete_submission_count" in value:
        out["successfulDeleteSubmissionCount"] = value[
            "successful_delete_submission_count"
        ]
    if "failed_delete_submission_count" in value:
        out["failedDeleteSubmissionCount"] = value["failed_delete_submission_count"]
    return out


def deserialize_json(data: dict) -> SubmissionSummary:
    out: SubmissionSummary = {}  # type: ignore[typeddict-item]
    if "successfulStartSubmissionCount" in data:
        out["successful_start_submission_count"] = data[
            "successfulStartSubmissionCount"
        ]
    if "failedStartSubmissionCount" in data:
        out["failed_start_submission_count"] = data["failedStartSubmissionCount"]
    if "pendingStartSubmissionCount" in data:
        out["pending_start_submission_count"] = data["pendingStartSubmissionCount"]
    if "successfulCancelSubmissionCount" in data:
        out["successful_cancel_submission_count"] = data[
            "successfulCancelSubmissionCount"
        ]
    if "failedCancelSubmissionCount" in data:
        out["failed_cancel_submission_count"] = data["failedCancelSubmissionCount"]
    if "successfulDeleteSubmissionCount" in data:
        out["successful_delete_submission_count"] = data[
            "successfulDeleteSubmissionCount"
        ]
    if "failedDeleteSubmissionCount" in data:
        out["failed_delete_submission_count"] = data["failedDeleteSubmissionCount"]
    return out
