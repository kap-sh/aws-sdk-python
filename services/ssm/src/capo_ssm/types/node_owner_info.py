"""Generated from Smithy shape ``com.amazonaws.ssm#NodeOwnerInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.node_account_id
    import capo_ssm.types.node_organizational_unit_id
    import capo_ssm.types.node_organizational_unit_path


class NodeOwnerInfo(TypedDict, closed=True):
    account_id: NotRequired["capo_ssm.types.node_account_id.NodeAccountId"]
    """<p>The ID of the Amazon Web Services account that owns the managed node.</p>"""
    organizational_unit_id: NotRequired[
        "capo_ssm.types.node_organizational_unit_id.NodeOrganizationalUnitId"
    ]
    """<p>The ID of the organization unit (OU) that the account is part of.</p>"""
    organizational_unit_path: NotRequired[
        "capo_ssm.types.node_organizational_unit_path.NodeOrganizationalUnitPath"
    ]
    """<p>The path for the organizational unit (OU) that owns the managed node. The path for the OU is built using the IDs of the organization, root, and all OUs in the path down to and including the OU. For example:</p> <p> <code>o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeOwnerInfo) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "organizational_unit_id" in value:
        out["OrganizationalUnitId"] = value["organizational_unit_id"]
    if "organizational_unit_path" in value:
        out["OrganizationalUnitPath"] = value["organizational_unit_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeOwnerInfo:
    out: NodeOwnerInfo = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "OrganizationalUnitId" in data:
        out["organizational_unit_id"] = data["OrganizationalUnitId"]
    if "OrganizationalUnitPath" in data:
        out["organizational_unit_path"] = data["OrganizationalUnitPath"]
    return out
