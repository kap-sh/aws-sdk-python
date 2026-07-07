"""Generated from Smithy shape ``com.amazonaws.neptune#DomainMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class DomainMembership(TypedDict, closed=True):
    domain: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The identifier of the Active Directory Domain.</p>"""
    status: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The status of the DB instance's Active Directory Domain membership, such as joined, pending-join, failed etc).</p>"""
    fqdn: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The fully qualified domain name of the Active Directory Domain.</p>"""
    iam_role_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the IAM role to be used when making API calls to the Directory Service.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "domain" in value:
        pairs.append((f"{prefix}.Domain", str(value["domain"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "fqdn" in value:
        pairs.append((f"{prefix}.FQDN", str(value["fqdn"])))
    if "iam_role_name" in value:
        pairs.append((f"{prefix}.IAMRoleName", str(value["iam_role_name"])))


def deserialize_query(el: Element) -> DomainMembership:
    out: DomainMembership = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_fqdn = el.find("FQDN")
    if child_fqdn is not None:
        out["fqdn"] = str(child_fqdn.text or "")
    child_iam_role_name = el.find("IAMRoleName")
    if child_iam_role_name is not None:
        out["iam_role_name"] = str(child_iam_role_name.text or "")
    return out
