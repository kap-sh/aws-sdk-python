"""Generated from Smithy shape ``com.amazonaws.transcribe#GetVocabularyFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.vocabulary_filter_name


class GetVocabularyFilterRequest(TypedDict, closed=True):
    vocabulary_filter_name: (
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    )
    """<p>The name of the custom vocabulary filter you want information about. Custom vocabulary filter names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetVocabularyFilterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetVocabularyFilterRequest:
    out: GetVocabularyFilterRequest = {}  # type: ignore[typeddict-item]
    return out
