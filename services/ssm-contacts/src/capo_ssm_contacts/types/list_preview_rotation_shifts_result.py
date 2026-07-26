"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPreviewRotationShiftsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.rotation_shifts


class ListPreviewRotationShiftsResult(TypedDict, closed=True):
    rotation_shifts: NotRequired[
        "capo_ssm_contacts.types.rotation_shifts.RotationShifts"
    ]
    """<p>Details about a rotation shift, including times, types, and contacts.</p>"""
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of items to return. This token is used to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPreviewRotationShiftsResult) -> dict:
    out: dict = {}
    if "rotation_shifts" in value:
        import capo_ssm_contacts.types.rotation_shifts

        out["RotationShifts"] = (
            capo_ssm_contacts.types.rotation_shifts.serialize_aws_json_1_1(
                value["rotation_shifts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPreviewRotationShiftsResult:
    out: ListPreviewRotationShiftsResult = {}  # type: ignore[typeddict-item]
    if "RotationShifts" in data:
        import capo_ssm_contacts.types.rotation_shifts

        out["rotation_shifts"] = (
            capo_ssm_contacts.types.rotation_shifts.deserialize_aws_json_1_1(
                data["RotationShifts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
