"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RecommendationFeedbackSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.reactions
    import aws_sdk_codeguru_reviewer.types.recommendation_id
    import aws_sdk_codeguru_reviewer.types.user_id


class RecommendationFeedbackSummary(TypedDict, closed=True):
    recommendation_id: NotRequired[
        "aws_sdk_codeguru_reviewer.types.recommendation_id.RecommendationId"
    ]
    """<p>The recommendation ID that can be used to track the provided recommendations. Later on it can be used to collect the feedback.</p>"""
    reactions: NotRequired["aws_sdk_codeguru_reviewer.types.reactions.Reactions"]
    """<p>List for storing reactions. Reactions are utf-8 text code for emojis.</p>"""
    user_id: NotRequired["aws_sdk_codeguru_reviewer.types.user_id.UserId"]
    r"""<p>The ID of the user that gave the feedback.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationFeedbackSummary) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "reactions" in value:
        import aws_sdk_codeguru_reviewer.types.reactions

        out["Reactions"] = aws_sdk_codeguru_reviewer.types.reactions.serialize_json(
            value["reactions"]
        )
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> RecommendationFeedbackSummary:
    out: RecommendationFeedbackSummary = {}  # type: ignore[typeddict-item]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "Reactions" in data:
        import aws_sdk_codeguru_reviewer.types.reactions

        out["reactions"] = aws_sdk_codeguru_reviewer.types.reactions.deserialize_json(
            data["Reactions"]
        )
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
