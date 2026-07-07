"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateCommentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comment


class UpdateCommentOutput(TypedDict, closed=True):
    comment: NotRequired["aws_sdk_codecommit.types.comment.Comment"]
    """<p>Information about the updated comment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCommentOutput) -> dict:
    out: dict = {}
    if "comment" in value:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.serialize_aws_json_1_1(
            value["comment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCommentOutput:
    out: UpdateCommentOutput = {}  # type: ignore[typeddict-item]
    if "comment" in data:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.deserialize_aws_json_1_1(
            data["comment"]
        )
    return out
