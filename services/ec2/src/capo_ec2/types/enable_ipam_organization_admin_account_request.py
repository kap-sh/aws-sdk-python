"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class EnableIpamOrganizationAdminAccountRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    delegated_admin_account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Organizations member account ID that you want to enable as the IPAM account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableIpamOrganizationAdminAccountRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "delegated_admin_account_id" in value:
        pairs.append(
            (
                f"{prefix}.DelegatedAdminAccountId",
                str(value["delegated_admin_account_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> EnableIpamOrganizationAdminAccountRequest:
    out: EnableIpamOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_delegated_admin_account_id = el.find("DelegatedAdminAccountId")
    if child_delegated_admin_account_id is not None:
        out["delegated_admin_account_id"] = str(
            child_delegated_admin_account_id.text or ""
        )
    return out
