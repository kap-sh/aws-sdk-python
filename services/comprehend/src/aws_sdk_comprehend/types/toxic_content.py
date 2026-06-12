"""Generated from Smithy shape ``com.amazonaws.comprehend#ToxicContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.toxic_content_type


class ToxicContent(TypedDict):
    name: NotRequired["aws_sdk_comprehend.types.toxic_content_type.ToxicContentType"]
    """<p>The name of the toxic content type.</p>"""
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p> Model confidence in the detected content type. Value range is zero to one, where one is highest confidence.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicContent) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_comprehend.types.toxic_content_type

        out["Name"] = (
            aws_sdk_comprehend.types.toxic_content_type.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ToxicContent:
    out: ToxicContent = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_comprehend.types.toxic_content_type

        out["name"] = (
            aws_sdk_comprehend.types.toxic_content_type.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    return out
