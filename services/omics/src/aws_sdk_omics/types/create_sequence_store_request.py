"""Generated from Smithy shape ``com.amazonaws.omics#CreateSequenceStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.client_token
    import aws_sdk_omics.types.e_tag_algorithm_family
    import aws_sdk_omics.types.fallback_location
    import aws_sdk_omics.types.propagated_set_level_tags
    import aws_sdk_omics.types.s3_access_config
    import aws_sdk_omics.types.sequence_store_description
    import aws_sdk_omics.types.sequence_store_name
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.tag_map


class CreateSequenceStoreRequest(TypedDict, closed=True):
    name: "aws_sdk_omics.types.sequence_store_name.SequenceStoreName"
    """<p>A name for the store.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>A description for the store.</p>"""
    sse_config: NotRequired["aws_sdk_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Tags for the store. You can configure up to 50 tags.</p>"""
    client_token: NotRequired["aws_sdk_omics.types.client_token.ClientToken"]
    """<p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>"""
    fallback_location: NotRequired[
        "aws_sdk_omics.types.fallback_location.FallbackLocation"
    ]
    """<p>An S3 location that is used to store files that have failed a direct upload. You can add or change the <code>fallbackLocation</code> after creating a sequence store. This is not required if you are uploading files from a different S3 bucket.</p>"""
    e_tag_algorithm_family: NotRequired[
        "aws_sdk_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    r"""<p>The ETag algorithm family to use for ingested read sets. The default value is MD5up. For more information on ETags, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/etags-and-provenance.html\">ETags and data provenance</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    propagated_set_level_tags: NotRequired[
        "aws_sdk_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
    ]
    """<p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store. These tags can be used as input to add metadata to your read sets.</p>"""
    s3_access_config: NotRequired["aws_sdk_omics.types.s3_access_config.S3AccessConfig"]
    """<p>S3 access configuration parameters. This specifies the parameters needed to access logs stored in S3 buckets. The S3 bucket must be in the same region and account as the sequence store. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSequenceStoreRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sse_config" in value:
        import aws_sdk_omics.types.sse_config

        out["sseConfig"] = aws_sdk_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    if "propagated_set_level_tags" in value:
        import aws_sdk_omics.types.propagated_set_level_tags

        out["propagatedSetLevelTags"] = (
            aws_sdk_omics.types.propagated_set_level_tags.serialize_json(
                value["propagated_set_level_tags"]
            )
        )
    if "s3_access_config" in value:
        import aws_sdk_omics.types.s3_access_config

        out["s3AccessConfig"] = aws_sdk_omics.types.s3_access_config.serialize_json(
            value["s3_access_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateSequenceStoreRequest:
    out: CreateSequenceStoreRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSequenceStoreRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "sseConfig" in data:
        import aws_sdk_omics.types.sse_config

        out["sse_config"] = aws_sdk_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "fallbackLocation" in data:
        out["fallback_location"] = data["fallbackLocation"]
    if "eTagAlgorithmFamily" in data:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    if "propagatedSetLevelTags" in data:
        import aws_sdk_omics.types.propagated_set_level_tags

        out["propagated_set_level_tags"] = (
            aws_sdk_omics.types.propagated_set_level_tags.deserialize_json(
                data["propagatedSetLevelTags"]
            )
        )
    if "s3AccessConfig" in data:
        import aws_sdk_omics.types.s3_access_config

        out["s3_access_config"] = aws_sdk_omics.types.s3_access_config.deserialize_json(
            data["s3AccessConfig"]
        )
    return out
