"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedIamRoleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.timestamp


class UnusedIamRoleDetails(TypedDict, closed=True):
    last_accessed: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the role was last accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedIamRoleDetails) -> dict:
    out: dict = {}
    if "last_accessed" in value:
        import capo_accessanalyzer.types.timestamp

        out["lastAccessed"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["last_accessed"]
        )
    return out


def deserialize_json(data: dict) -> UnusedIamRoleDetails:
    out: UnusedIamRoleDetails = {}  # type: ignore[typeddict-item]
    if "lastAccessed" in data:
        import capo_accessanalyzer.types.timestamp

        out["last_accessed"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["lastAccessed"]
        )
    return out
