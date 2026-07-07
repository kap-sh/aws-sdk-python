"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Transcript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.result_list


class Transcript(TypedDict, closed=True):
    results: NotRequired["aws_sdk_transcribe_streaming.types.result_list.ResultList"]
    """<p>Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transcript) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_transcribe_streaming.types.result_list

        out["Results"] = aws_sdk_transcribe_streaming.types.result_list.serialize_json(
            value["results"]
        )
    return out


def deserialize_json(data: dict) -> Transcript:
    out: Transcript = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_transcribe_streaming.types.result_list

        out["results"] = (
            aws_sdk_transcribe_streaming.types.result_list.deserialize_json(
                data["Results"]
            )
        )
    return out
