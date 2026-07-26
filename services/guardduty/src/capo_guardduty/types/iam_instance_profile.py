"""Generated from Smithy shape ``com.amazonaws.guardduty#IamInstanceProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class IamInstanceProfile(TypedDict, closed=True):
    arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The profile ARN of the EC2 instance.</p>"""
    id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The profile ID of the EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamInstanceProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> IamInstanceProfile:
    out: IamInstanceProfile = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    return out
