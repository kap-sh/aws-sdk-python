"""Generated from Smithy shape ``com.amazonaws.rekognition#UserMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.matched_user
    import aws_sdk_rekognition.types.percent


class UserMatch(TypedDict, closed=True):
    similarity: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p> Describes the UserID metadata.</p>"""
    user: NotRequired["aws_sdk_rekognition.types.matched_user.MatchedUser"]
    """<p> Confidence in the match of this UserID with the input face. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserMatch) -> dict:
    out: dict = {}
    if "similarity" in value:
        out["Similarity"] = value["similarity"]
    if "user" in value:
        import aws_sdk_rekognition.types.matched_user

        out["User"] = aws_sdk_rekognition.types.matched_user.serialize_aws_json_1_1(
            value["user"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserMatch:
    out: UserMatch = {}  # type: ignore[typeddict-item]
    if "Similarity" in data:
        out["similarity"] = data["Similarity"]
    if "User" in data:
        import aws_sdk_rekognition.types.matched_user

        out["user"] = aws_sdk_rekognition.types.matched_user.deserialize_aws_json_1_1(
            data["User"]
        )
    return out
