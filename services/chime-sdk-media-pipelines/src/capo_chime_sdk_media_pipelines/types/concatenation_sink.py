"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSink``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.concatenation_sink_type
    import capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration


class ConcatenationSink(TypedDict, closed=True):
    type: "capo_chime_sdk_media_pipelines.types.concatenation_sink_type.ConcatenationSinkType"
    """<p>The type of data sink in the configuration object.</p>"""
    s3_bucket_sink_configuration: "capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration.S3BucketSinkConfiguration"
    """<p>The configuration settings for an Amazon S3 bucket sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSink) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.concatenation_sink_type

    out["Type"] = (
        capo_chime_sdk_media_pipelines.types.concatenation_sink_type.serialize_json(
            value["type"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration

    out["S3BucketSinkConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration.serialize_json(
            value["s3_bucket_sink_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConcatenationSink:
    out: ConcatenationSink = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_chime_sdk_media_pipelines.types.concatenation_sink_type

        out["type"] = (
            capo_chime_sdk_media_pipelines.types.concatenation_sink_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("ConcatenationSink.type required")
    if "S3BucketSinkConfiguration" in data:
        import capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration

        out["s3_bucket_sink_configuration"] = (
            capo_chime_sdk_media_pipelines.types.s3_bucket_sink_configuration.deserialize_json(
                data["S3BucketSinkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ConcatenationSink.s3_bucket_sink_configuration required"
        )
    return out
