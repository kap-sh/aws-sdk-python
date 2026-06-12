"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedIamUserPasswordDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.timestamp


class UnusedIamUserPasswordDetails(TypedDict):
    last_accessed: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the password was last accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedIamUserPasswordDetails) -> dict:
    out: dict = {}
    if "last_accessed" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["lastAccessed"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["last_accessed"]
        )
    return out


def deserialize_json(data: dict) -> UnusedIamUserPasswordDetails:
    out: UnusedIamUserPasswordDetails = {}  # type: ignore[typeddict-item]
    if "lastAccessed" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["last_accessed"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["lastAccessed"]
        )
    return out
