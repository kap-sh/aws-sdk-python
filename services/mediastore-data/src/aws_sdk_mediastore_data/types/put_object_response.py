"""Generated from Smithy shape ``com.amazonaws.mediastoredata#PutObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediastore_data.types.e_tag
    import aws_sdk_mediastore_data.types.sha256_hash
    import aws_sdk_mediastore_data.types.storage_class


class PutObjectResponse(TypedDict, closed=True):
    content_sha256: NotRequired["aws_sdk_mediastore_data.types.sha256_hash.SHA256Hash"]
    """<p>The SHA256 digest of the object that is persisted.</p>"""
    e_tag: NotRequired["aws_sdk_mediastore_data.types.e_tag.ETag"]
    """<p>Unique identifier of the object in the container.</p>"""
    storage_class: NotRequired[
        "aws_sdk_mediastore_data.types.storage_class.StorageClass"
    ]
    """<p>The storage class where the object was persisted. The class should be “Temporal”.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutObjectResponse) -> dict:
    out: dict = {}
    if "content_sha256" in value:
        out["ContentSHA256"] = value["content_sha256"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "storage_class" in value:
        import aws_sdk_mediastore_data.types.storage_class

        out["StorageClass"] = (
            aws_sdk_mediastore_data.types.storage_class.serialize_json(
                value["storage_class"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutObjectResponse:
    out: PutObjectResponse = {}  # type: ignore[typeddict-item]
    if "ContentSHA256" in data:
        out["content_sha256"] = data["ContentSHA256"]
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "StorageClass" in data:
        import aws_sdk_mediastore_data.types.storage_class

        out["storage_class"] = (
            aws_sdk_mediastore_data.types.storage_class.deserialize_json(
                data["StorageClass"]
            )
        )
    return out
