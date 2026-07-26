"""Generated from Smithy shape ``com.amazonaws.mpa#IamIdentityCenterForGet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.string


class IamIdentityCenterForGet(TypedDict, closed=True):
    instance_arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the IAM Identity Center instance.</p>"""
    approval_portal_url: NotRequired["capo_mpa.types.string.String"]
    """<p>URL for the approval portal associated with the IAM Identity Center instance.</p>"""
    region: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Web Services Region where the IAM Identity Center instance is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamIdentityCenterForGet) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "approval_portal_url" in value:
        out["ApprovalPortalUrl"] = value["approval_portal_url"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> IamIdentityCenterForGet:
    out: IamIdentityCenterForGet = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "ApprovalPortalUrl" in data:
        out["approval_portal_url"] = data["ApprovalPortalUrl"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
