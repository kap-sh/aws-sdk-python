"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedIamUserAccessKeyDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.timestamp


class UnusedIamUserAccessKeyDetails(TypedDict):
    access_key_id: "str"
    """<p>The ID of the access key for which the unused access finding was generated.</p>"""
    last_accessed: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the access key was last accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedIamUserAccessKeyDetails) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    if "last_accessed" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["lastAccessed"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["last_accessed"]
        )
    return out


def deserialize_json(data: dict) -> UnusedIamUserAccessKeyDetails:
    out: UnusedIamUserAccessKeyDetails = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    else:
        raise DeserializationError(
            "UnusedIamUserAccessKeyDetails.access_key_id required"
        )
    if "lastAccessed" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["last_accessed"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["lastAccessed"]
        )
    return out
