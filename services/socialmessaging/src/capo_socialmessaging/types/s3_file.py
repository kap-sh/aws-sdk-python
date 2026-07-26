"""Generated from Smithy shape ``com.amazonaws.socialmessaging#S3File``."""

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError


class S3File(TypedDict, closed=True):
    bucket_name: "str"
    """<p>The bucket name.</p>"""
    key: "str"
    """<p>The S3 key prefix that defines the storage location of your media files. The prefix works like a folder path in S3, and is combined with the WhatsApp mediaId to create the final file path.</p> <p>For example, if a media file's WhatsApp mediaId is <code>123.ogg</code>, and the key is <code>audio/example.ogg</code>, the final file path is <code>audio/example.ogg123.ogg</code>.</p> <p>For the same mediaId, a key of <code>audio/</code> results in the file path <code>audio/123.ogg</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3File) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3File:
    out: S3File = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3File.bucket_name required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3File.key required")
    return out
