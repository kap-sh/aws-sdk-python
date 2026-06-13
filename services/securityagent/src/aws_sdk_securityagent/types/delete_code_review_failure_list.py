"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteCodeReviewFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.delete_code_review_failure

DeleteCodeReviewFailureList: TypeAlias = list[
    "aws_sdk_securityagent.types.delete_code_review_failure.DeleteCodeReviewFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeReviewFailureList) -> list:
    import aws_sdk_securityagent.types.delete_code_review_failure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.delete_code_review_failure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteCodeReviewFailureList:
    import aws_sdk_securityagent.types.delete_code_review_failure

    out: DeleteCodeReviewFailureList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.delete_code_review_failure.deserialize_json(
                item
            )
        )
    return out
