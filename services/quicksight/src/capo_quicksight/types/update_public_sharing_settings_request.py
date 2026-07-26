"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdatePublicSharingSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean


class UpdatePublicSharingSettingsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID associated with your Amazon Quick Sight subscription.</p>"""
    public_sharing_enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether public sharing is turned on for an Quick account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePublicSharingSettingsRequest) -> dict:
    out: dict = {}
    out["PublicSharingEnabled"] = value.get("public_sharing_enabled", False)
    return out


def deserialize_json(data: dict) -> UpdatePublicSharingSettingsRequest:
    out: UpdatePublicSharingSettingsRequest = {}  # type: ignore[typeddict-item]
    if "PublicSharingEnabled" in data:
        out["public_sharing_enabled"] = data["PublicSharingEnabled"]
    else:
        out["public_sharing_enabled"] = False
    return out
