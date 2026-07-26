"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TranscriptSourceSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.s3_bucket_transcript_source


class TranscriptSourceSetting(TypedDict, closed=True):
    s3_bucket_transcript_source: NotRequired[
        "capo_lex_models_v2.types.s3_bucket_transcript_source.S3BucketTranscriptSource"
    ]
    """<p>Indicates the setting of the Amazon S3 bucket where the transcript is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptSourceSetting) -> dict:
    out: dict = {}
    if "s3_bucket_transcript_source" in value:
        import capo_lex_models_v2.types.s3_bucket_transcript_source

        out["s3BucketTranscriptSource"] = (
            capo_lex_models_v2.types.s3_bucket_transcript_source.serialize_json(
                value["s3_bucket_transcript_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranscriptSourceSetting:
    out: TranscriptSourceSetting = {}  # type: ignore[typeddict-item]
    if "s3BucketTranscriptSource" in data:
        import capo_lex_models_v2.types.s3_bucket_transcript_source

        out["s3_bucket_transcript_source"] = (
            capo_lex_models_v2.types.s3_bucket_transcript_source.deserialize_json(
                data["s3BucketTranscriptSource"]
            )
        )
    return out
