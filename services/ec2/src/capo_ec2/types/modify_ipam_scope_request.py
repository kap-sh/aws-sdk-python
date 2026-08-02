"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.external_authority_configuration
    import capo_ec2.types.ipam_scope_id
    import capo_ec2.types.string


class ModifyIpamScopeRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope you want to modify.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the scope you want to modify.</p>"""
    external_authority_configuration: NotRequired[
        "capo_ec2.types.external_authority_configuration.ExternalAuthorityConfiguration"
    ]
    """<p>The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.</p> <p>In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to Amazon Web Services while using Amazon VPC IPAM to manage subnets within those ranges.</p>"""
    remove_external_authority_configuration: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Remove the external authority configuration. <code>true</code> to remove.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamScopeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_scope_id" in value:
        pairs.append((f"{key_prefix}IpamScopeId", str(value["ipam_scope_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "external_authority_configuration" in value:
        import capo_ec2.types.external_authority_configuration

        capo_ec2.types.external_authority_configuration.serialize_ec2_query(
            value["external_authority_configuration"],
            pairs,
            f"{key_prefix}ExternalAuthorityConfiguration",
        )
    if "remove_external_authority_configuration" in value:
        pairs.append(
            (
                f"{key_prefix}RemoveExternalAuthorityConfiguration",
                "true" if value["remove_external_authority_configuration"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamScopeRequest:
    out: ModifyIpamScopeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_scope_id = el.find("IpamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_external_authority_configuration = el.find("ExternalAuthorityConfiguration")
    if child_external_authority_configuration is not None:
        import capo_ec2.types.external_authority_configuration

        out["external_authority_configuration"] = (
            capo_ec2.types.external_authority_configuration.deserialize_ec2_query(
                child_external_authority_configuration
            )
        )
    child_remove_external_authority_configuration = el.find(
        "RemoveExternalAuthorityConfiguration"
    )
    if child_remove_external_authority_configuration is not None:
        out["remove_external_authority_configuration"] = (
            child_remove_external_authority_configuration.text or ""
        ).lower() == "true"
    return out
