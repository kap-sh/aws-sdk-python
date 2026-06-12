"""Generated from Smithy shape ``com.amazonaws.mpa#UpdateApprovalTeamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.string


class UpdateApprovalTeamResponse(TypedDict):
    version_id: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Version ID for the team that was created. When an approval team is updated, the version ID changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApprovalTeamResponse) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> UpdateApprovalTeamResponse:
    out: UpdateApprovalTeamResponse = {}  # type: ignore[typeddict-item]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
