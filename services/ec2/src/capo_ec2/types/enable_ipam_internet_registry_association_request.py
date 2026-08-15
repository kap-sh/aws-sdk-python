"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamInternetRegistryAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_internet_registry_association_id
    import capo_ec2.types.string


class EnableIpamInternetRegistryAssociationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_internet_registry_association_id: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_id.IpamInternetRegistryAssociationId"
    ]
    """<p>The ID of the IPAM internet registry association to enable.</p>"""
    rpki_version: NotRequired["capo_ec2.types.string.String"]
    """<p>The RPKI version to use from the Parent Response XML.</p>"""
    service_uri: NotRequired["capo_ec2.types.string.String"]
    """<p>The RPKI service URI for the publication point from the Parent Response XML.</p>"""
    child_handle: NotRequired["capo_ec2.types.string.String"]
    """<p>The child handle for the BPKI certificate hierarchy from the Parent Response XML.</p>"""
    parent_handle: NotRequired["capo_ec2.types.string.String"]
    """<p>The parent handle for the BPKI certificate hierarchy from the Parent Response XML.</p>"""
    parent_bpki_ta: NotRequired["capo_ec2.types.string.String"]
    """<p>The parent BPKI Trust Anchor certificate in PEM format from the Parent Response XML.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableIpamInternetRegistryAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_internet_registry_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamInternetRegistryAssociationId",
                str(value["ipam_internet_registry_association_id"]),
            )
        )
    if "rpki_version" in value:
        pairs.append((f"{key_prefix}RpkiVersion", str(value["rpki_version"])))
    if "service_uri" in value:
        pairs.append((f"{key_prefix}ServiceUri", str(value["service_uri"])))
    if "child_handle" in value:
        pairs.append((f"{key_prefix}ChildHandle", str(value["child_handle"])))
    if "parent_handle" in value:
        pairs.append((f"{key_prefix}ParentHandle", str(value["parent_handle"])))
    if "parent_bpki_ta" in value:
        pairs.append((f"{key_prefix}ParentBpkiTa", str(value["parent_bpki_ta"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> EnableIpamInternetRegistryAssociationRequest:
    out: EnableIpamInternetRegistryAssociationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_internet_registry_association_id = el.find(
        "IpamInternetRegistryAssociationId"
    )
    if child_ipam_internet_registry_association_id is not None:
        out["ipam_internet_registry_association_id"] = str(
            child_ipam_internet_registry_association_id.text or ""
        )
    child_rpki_version = el.find("RpkiVersion")
    if child_rpki_version is not None:
        out["rpki_version"] = str(child_rpki_version.text or "")
    child_service_uri = el.find("ServiceUri")
    if child_service_uri is not None:
        out["service_uri"] = str(child_service_uri.text or "")
    child_child_handle = el.find("ChildHandle")
    if child_child_handle is not None:
        out["child_handle"] = str(child_child_handle.text or "")
    child_parent_handle = el.find("ParentHandle")
    if child_parent_handle is not None:
        out["parent_handle"] = str(child_parent_handle.text or "")
    child_parent_bpki_ta = el.find("ParentBpkiTa")
    if child_parent_bpki_ta is not None:
        out["parent_bpki_ta"] = str(child_parent_bpki_ta.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
