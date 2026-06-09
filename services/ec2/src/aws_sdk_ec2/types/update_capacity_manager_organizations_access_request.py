"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerOrganizationsAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.string


class UpdateCapacityManagerOrganizationsAccessRequest(TypedDict):
    organizations_access: NotRequired["aws_sdk_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p> Specifies whether to enable or disable cross-account access for Amazon Web Services Organizations. When enabled, Capacity Manager aggregates data from all accounts in your organization. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateCapacityManagerOrganizationsAccessRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "organizations_access" in value:
        pairs.append(
            (
                f"{prefix}.OrganizationsAccess",
                "true" if value["organizations_access"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(
    el: Element,
) -> UpdateCapacityManagerOrganizationsAccessRequest:
    out: UpdateCapacityManagerOrganizationsAccessRequest = {}  # type: ignore[typeddict-item]
    child_organizations_access = el.find("OrganizationsAccess")
    if child_organizations_access is not None:
        out["organizations_access"] = (
            child_organizations_access.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
