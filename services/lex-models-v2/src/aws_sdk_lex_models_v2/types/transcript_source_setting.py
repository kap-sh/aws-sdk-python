"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TranscriptSourceSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.s3_bucket_transcript_source


class TranscriptSourceSetting(TypedDict):
    s3_bucket_transcript_source: NotRequired[
        "aws_sdk_lex_models_v2.types.s3_bucket_transcript_source.S3BucketTranscriptSource"
    ]
    """<p>Indicates the setting of the Amazon S3 bucket where the transcript is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptSourceSetting) -> dict:
    out: dict = {}
    if "s3_bucket_transcript_source" in value:
        import aws_sdk_lex_models_v2.types.s3_bucket_transcript_source

        out["s3BucketTranscriptSource"] = (
            aws_sdk_lex_models_v2.types.s3_bucket_transcript_source.serialize_json(
                value["s3_bucket_transcript_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranscriptSourceSetting:
    out: TranscriptSourceSetting = {}  # type: ignore[typeddict-item]
    if "s3BucketTranscriptSource" in data:
        import aws_sdk_lex_models_v2.types.s3_bucket_transcript_source

        out["s3_bucket_transcript_source"] = (
            aws_sdk_lex_models_v2.types.s3_bucket_transcript_source.deserialize_json(
                data["s3BucketTranscriptSource"]
            )
        )
    return out
