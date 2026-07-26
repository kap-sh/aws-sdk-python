"""Generated from Smithy shape ``com.amazonaws.omics#UpdateSequenceStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.client_token
    import capo_omics.types.fallback_location
    import capo_omics.types.propagated_set_level_tags
    import capo_omics.types.s3_access_config
    import capo_omics.types.sequence_store_description
    import capo_omics.types.sequence_store_id
    import capo_omics.types.sequence_store_name


class UpdateSequenceStoreRequest(TypedDict, closed=True):
    id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The ID of the sequence store.</p>"""
    name: NotRequired["capo_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>A name for the sequence store.</p>"""
    description: NotRequired[
        "capo_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>A description for the sequence store.</p>"""
    client_token: NotRequired["capo_omics.types.client_token.ClientToken"]
    """<p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>"""
    fallback_location: NotRequired[
        "capo_omics.types.fallback_location.FallbackLocation"
    ]
    """<p>The S3 URI of a bucket and folder to store Read Sets that fail to upload.</p>"""
    propagated_set_level_tags: NotRequired[
        "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
    ]
    """<p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>"""
    s3_access_config: NotRequired["capo_omics.types.s3_access_config.S3AccessConfig"]
    """<p>S3 access configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSequenceStoreRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "propagated_set_level_tags" in value:
        import capo_omics.types.propagated_set_level_tags

        out["propagatedSetLevelTags"] = (
            capo_omics.types.propagated_set_level_tags.serialize_json(
                value["propagated_set_level_tags"]
            )
        )
    if "s3_access_config" in value:
        import capo_omics.types.s3_access_config

        out["s3AccessConfig"] = capo_omics.types.s3_access_config.serialize_json(
            value["s3_access_config"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSequenceStoreRequest:
    out: UpdateSequenceStoreRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "fallbackLocation" in data:
        out["fallback_location"] = data["fallbackLocation"]
    if "propagatedSetLevelTags" in data:
        import capo_omics.types.propagated_set_level_tags

        out["propagated_set_level_tags"] = (
            capo_omics.types.propagated_set_level_tags.deserialize_json(
                data["propagatedSetLevelTags"]
            )
        )
    if "s3AccessConfig" in data:
        import capo_omics.types.s3_access_config

        out["s3_access_config"] = capo_omics.types.s3_access_config.deserialize_json(
            data["s3AccessConfig"]
        )
    return out
