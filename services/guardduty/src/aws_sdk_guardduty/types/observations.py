"""Generated from Smithy shape ``com.amazonaws.guardduty#Observations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.observation_texts


class Observations(TypedDict):
    text: NotRequired["aws_sdk_guardduty.types.observation_texts.ObservationTexts"]
    """<p>The text that was unusual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Observations) -> dict:
    out: dict = {}
    if "text" in value:
        import aws_sdk_guardduty.types.observation_texts

        out["text"] = aws_sdk_guardduty.types.observation_texts.serialize_json(
            value["text"]
        )
    return out


def deserialize_json(data: dict) -> Observations:
    out: Observations = {}  # type: ignore[typeddict-item]
    if "text" in data:
        import aws_sdk_guardduty.types.observation_texts

        out["text"] = aws_sdk_guardduty.types.observation_texts.deserialize_json(
            data["text"]
        )
    return out
