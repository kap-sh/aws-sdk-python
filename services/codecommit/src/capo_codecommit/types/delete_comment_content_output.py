"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteCommentContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.comment


class DeleteCommentContentOutput(TypedDict, closed=True):
    comment: NotRequired["capo_codecommit.types.comment.Comment"]
    """<p>Information about the comment you just deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCommentContentOutput) -> dict:
    out: dict = {}
    if "comment" in value:
        import capo_codecommit.types.comment

        out["comment"] = capo_codecommit.types.comment.serialize_aws_json_1_1(
            value["comment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCommentContentOutput:
    out: DeleteCommentContentOutput = {}  # type: ignore[typeddict-item]
    if "comment" in data:
        import capo_codecommit.types.comment

        out["comment"] = capo_codecommit.types.comment.deserialize_aws_json_1_1(
            data["comment"]
        )
    return out
