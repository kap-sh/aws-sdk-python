"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#RelevanceMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_size


class RelevanceMetric(TypedDict):
    audience_size: "aws_sdk_cleanroomsml.types.audience_size.AudienceSize"
    score: NotRequired["float"]
    """<p>The relevance score of the generated audience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelevanceMetric) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.audience_size

    out["audienceSize"] = aws_sdk_cleanroomsml.types.audience_size.serialize_json(
        value["audience_size"]
    )
    if "score" in value:
        out["score"] = value["score"]
    return out


def deserialize_json(data: dict) -> RelevanceMetric:
    out: RelevanceMetric = {}  # type: ignore[typeddict-item]
    if "audienceSize" in data:
        import aws_sdk_cleanroomsml.types.audience_size

        out["audience_size"] = (
            aws_sdk_cleanroomsml.types.audience_size.deserialize_json(
                data["audienceSize"]
            )
        )
    else:
        raise DeserializationError("RelevanceMetric.audience_size required")
    if "score" in data:
        out["score"] = data["score"]
    return out
