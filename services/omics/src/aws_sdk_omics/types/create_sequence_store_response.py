"""Generated from Smithy shape ``com.amazonaws.omics#CreateSequenceStoreResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.e_tag_algorithm_family
    import aws_sdk_omics.types.fallback_location
    import aws_sdk_omics.types.propagated_set_level_tags
    import aws_sdk_omics.types.sequence_store_arn
    import aws_sdk_omics.types.sequence_store_description
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.sequence_store_name
    import aws_sdk_omics.types.sequence_store_s3_access
    import aws_sdk_omics.types.sequence_store_status
    import aws_sdk_omics.types.sequence_store_status_message
    import aws_sdk_omics.types.sse_config


class CreateSequenceStoreResponse(TypedDict):
    id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The store's ID.</p>"""
    arn: "aws_sdk_omics.types.sequence_store_arn.SequenceStoreArn"
    """<p>The store's ARN.</p>"""
    name: NotRequired["aws_sdk_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>The store's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>The store's description.</p>"""
    sse_config: NotRequired["aws_sdk_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store. This contains the KMS key ARN that is used to encrypt read set objects.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the store was created.</p>"""
    fallback_location: NotRequired[
        "aws_sdk_omics.types.fallback_location.FallbackLocation"
    ]
    """<p>An S3 location that is used to store files that have failed a direct upload.</p>"""
    e_tag_algorithm_family: NotRequired[
        "aws_sdk_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    """<p>The algorithm family of the ETag.</p>"""
    status: NotRequired["aws_sdk_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>The status of the sequence store.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.sequence_store_status_message.SequenceStoreStatusMessage"
    ]
    """<p>The status message of the sequence store.</p>"""
    propagated_set_level_tags: NotRequired[
        "aws_sdk_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
    ]
    """<p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>"""
    s3_access: NotRequired[
        "aws_sdk_omics.types.sequence_store_s3_access.SequenceStoreS3Access"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSequenceStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sse_config" in value:
        import aws_sdk_omics.types.sse_config

        out["sseConfig"] = aws_sdk_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "propagated_set_level_tags" in value:
        import aws_sdk_omics.types.propagated_set_level_tags

        out["propagatedSetLevelTags"] = (
            aws_sdk_omics.types.propagated_set_level_tags.serialize_json(
                value["propagated_set_level_tags"]
            )
        )
    if "s3_access" in value:
        import aws_sdk_omics.types.sequence_store_s3_access

        out["s3Access"] = aws_sdk_omics.types.sequence_store_s3_access.serialize_json(
            value["s3_access"]
        )
    return out


def deserialize_json(data: dict) -> CreateSequenceStoreResponse:
    out: CreateSequenceStoreResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateSequenceStoreResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSequenceStoreResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "sseConfig" in data:
        import aws_sdk_omics.types.sse_config

        out["sse_config"] = aws_sdk_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("CreateSequenceStoreResponse.creation_time required")
    if "fallbackLocation" in data:
        out["fallback_location"] = data["fallbackLocation"]
    if "eTagAlgorithmFamily" in data:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "propagatedSetLevelTags" in data:
        import aws_sdk_omics.types.propagated_set_level_tags

        out["propagated_set_level_tags"] = (
            aws_sdk_omics.types.propagated_set_level_tags.deserialize_json(
                data["propagatedSetLevelTags"]
            )
        )
    if "s3Access" in data:
        import aws_sdk_omics.types.sequence_store_s3_access

        out["s3_access"] = (
            aws_sdk_omics.types.sequence_store_s3_access.deserialize_json(
                data["s3Access"]
            )
        )
    return out
