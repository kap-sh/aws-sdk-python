"""Generated from Smithy shape ``com.amazonaws.mpa#CreateApprovalTeamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.string


class CreateApprovalTeamResponse(TypedDict, closed=True):
    creation_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the team was created.</p>"""
    arn: NotRequired["capo_mpa.types.approval_team_arn.ApprovalTeamArn"]
    """<p>Amazon Resource Name (ARN) for the team that was created.</p>"""
    name: NotRequired["capo_mpa.types.string.String"]
    """<p>Name of the team that was created.</p>"""
    version_id: NotRequired["capo_mpa.types.string.String"]
    """<p>Version ID for the team that was created. When a team is updated, the version ID changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApprovalTeamResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_mpa.types.iso_timestamp

        out["CreationTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["creation_time"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> CreateApprovalTeamResponse:
    out: CreateApprovalTeamResponse = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import capo_mpa.types.iso_timestamp

        out["creation_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
