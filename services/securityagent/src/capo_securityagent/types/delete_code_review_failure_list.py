"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteCodeReviewFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.delete_code_review_failure

DeleteCodeReviewFailureList: TypeAlias = list[
    "capo_securityagent.types.delete_code_review_failure.DeleteCodeReviewFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeReviewFailureList) -> list:
    import capo_securityagent.types.delete_code_review_failure

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.delete_code_review_failure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteCodeReviewFailureList:
    import capo_securityagent.types.delete_code_review_failure

    out: DeleteCodeReviewFailureList = []
    for item in data:
        out.append(
            capo_securityagent.types.delete_code_review_failure.deserialize_json(item)
        )
    return out
