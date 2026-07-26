"""Generated from Smithy shape ``com.amazonaws.omics#UpdateSequenceStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.e_tag_algorithm_family
    import capo_omics.types.fallback_location
    import capo_omics.types.propagated_set_level_tags
    import capo_omics.types.sequence_store_arn
    import capo_omics.types.sequence_store_description
    import capo_omics.types.sequence_store_id
    import capo_omics.types.sequence_store_name
    import capo_omics.types.sequence_store_s3_access
    import capo_omics.types.sequence_store_status
    import capo_omics.types.sequence_store_status_message
    import capo_omics.types.sse_config


class UpdateSequenceStoreResponse(TypedDict, closed=True):
    id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The ID of the sequence store.</p>"""
    arn: "capo_omics.types.sequence_store_arn.SequenceStoreArn"
    """<p>The ARN of the sequence store.</p>"""
    name: NotRequired["capo_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>The name of the sequence store.</p>"""
    description: NotRequired[
        "capo_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>Description of the sequence store.</p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    creation_time: "datetime.datetime"
    """<p>The time when the store was created.</p>"""
    update_time: NotRequired["datetime.datetime"]
    """<p>The last-updated time of the Sequence Store.</p>"""
    propagated_set_level_tags: NotRequired[
        "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
    ]
    """<p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>"""
    status: NotRequired["capo_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>The status of the sequence store.</p>"""
    status_message: NotRequired[
        "capo_omics.types.sequence_store_status_message.SequenceStoreStatusMessage"
    ]
    """<p>The status message of the sequence store.</p>"""
    fallback_location: NotRequired[
        "capo_omics.types.fallback_location.FallbackLocation"
    ]
    """<p>The S3 URI of a bucket and folder to store Read Sets that fail to upload.</p>"""
    s3_access: NotRequired[
        "capo_omics.types.sequence_store_s3_access.SequenceStoreS3Access"
    ]
    e_tag_algorithm_family: NotRequired[
        "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    """<p>The ETag algorithm family to use on ingested read sets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSequenceStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sse_config" in value:
        import capo_omics.types.sse_config

        out["sseConfig"] = capo_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    import capo_omics.types._prelude.timestamp

    out["creationTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "update_time" in value:
        import capo_omics.types._prelude.timestamp

        out["updateTime"] = capo_omics.types._prelude.timestamp.serialize_json(
            value["update_time"]
        )
    if "propagated_set_level_tags" in value:
        import capo_omics.types.propagated_set_level_tags

        out["propagatedSetLevelTags"] = (
            capo_omics.types.propagated_set_level_tags.serialize_json(
                value["propagated_set_level_tags"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "s3_access" in value:
        import capo_omics.types.sequence_store_s3_access

        out["s3Access"] = capo_omics.types.sequence_store_s3_access.serialize_json(
            value["s3_access"]
        )
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    return out


def deserialize_json(data: dict) -> UpdateSequenceStoreResponse:
    out: UpdateSequenceStoreResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateSequenceStoreResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateSequenceStoreResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "sseConfig" in data:
        import capo_omics.types.sse_config

        out["sse_config"] = capo_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if "creationTime" in data:
        import capo_omics.types._prelude.timestamp

        out["creation_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("UpdateSequenceStoreResponse.creation_time required")
    if "updateTime" in data:
        import capo_omics.types._prelude.timestamp

        out["update_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    if "propagatedSetLevelTags" in data:
        import capo_omics.types.propagated_set_level_tags

        out["propagated_set_level_tags"] = (
            capo_omics.types.propagated_set_level_tags.deserialize_json(
                data["propagatedSetLevelTags"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "fallbackLocation" in data:
        out["fallback_location"] = data["fallbackLocation"]
    if "s3Access" in data:
        import capo_omics.types.sequence_store_s3_access

        out["s3_access"] = capo_omics.types.sequence_store_s3_access.deserialize_json(
            data["s3Access"]
        )
    if "eTagAlgorithmFamily" in data:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    return out
