"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#SendAlexaOfferToMasterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_signaling.types.answer


class SendAlexaOfferToMasterResponse(TypedDict, closed=True):
    answer: NotRequired["aws_sdk_kinesis_video_signaling.types.answer.Answer"]
    """<p>The base64-encoded SDP answer content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendAlexaOfferToMasterResponse) -> dict:
    out: dict = {}
    if "answer" in value:
        out["Answer"] = value["answer"]
    return out


def deserialize_json(data: dict) -> SendAlexaOfferToMasterResponse:
    out: SendAlexaOfferToMasterResponse = {}  # type: ignore[typeddict-item]
    if "Answer" in data:
        out["answer"] = data["Answer"]
    return out
