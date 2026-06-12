"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comment


class GetCommentOutput(TypedDict):
    comment: NotRequired["aws_sdk_codecommit.types.comment.Comment"]
    """<p>The contents of the comment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentOutput) -> dict:
    out: dict = {}
    if "comment" in value:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.serialize_aws_json_1_1(
            value["comment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentOutput:
    out: GetCommentOutput = {}  # type: ignore[typeddict-item]
    if "comment" in data:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.deserialize_aws_json_1_1(
            data["comment"]
        )
    return out
