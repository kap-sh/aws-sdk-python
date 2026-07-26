"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDeleteCodeReviewsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.code_review_id_list
    import capo_securityagent.types.delete_code_review_failure_list


class BatchDeleteCodeReviewsOutput(TypedDict, closed=True):
    deleted: NotRequired[
        "capo_securityagent.types.code_review_id_list.CodeReviewIdList"
    ]
    """<p>The list of identifiers of the code reviews that were successfully deleted.</p>"""
    failed: NotRequired[
        "capo_securityagent.types.delete_code_review_failure_list.DeleteCodeReviewFailureList"
    ]
    """<p>The list of code reviews that failed to delete, including the reason for each failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteCodeReviewsOutput) -> dict:
    out: dict = {}
    if "deleted" in value:
        import capo_securityagent.types.code_review_id_list

        out["deleted"] = capo_securityagent.types.code_review_id_list.serialize_json(
            value["deleted"]
        )
    if "failed" in value:
        import capo_securityagent.types.delete_code_review_failure_list

        out["failed"] = (
            capo_securityagent.types.delete_code_review_failure_list.serialize_json(
                value["failed"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteCodeReviewsOutput:
    out: BatchDeleteCodeReviewsOutput = {}  # type: ignore[typeddict-item]
    if "deleted" in data:
        import capo_securityagent.types.code_review_id_list

        out["deleted"] = capo_securityagent.types.code_review_id_list.deserialize_json(
            data["deleted"]
        )
    if "failed" in data:
        import capo_securityagent.types.delete_code_review_failure_list

        out["failed"] = (
            capo_securityagent.types.delete_code_review_failure_list.deserialize_json(
                data["failed"]
            )
        )
    return out
