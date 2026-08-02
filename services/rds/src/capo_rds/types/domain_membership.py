"""Generated from Smithy shape ``com.amazonaws.rds#DomainMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.string_list


class DomainMembership(TypedDict, closed=True):
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the Active Directory Domain.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the Active Directory Domain membership for the DB instance or cluster. Values include <code>joined</code>, <code>pending-join</code>, <code>failed</code>, and so on.</p>"""
    fqdn: NotRequired["capo_rds.types.string.String"]
    """<p>The fully qualified domain name (FQDN) of the Active Directory Domain.</p>"""
    iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role used when making API calls to the Directory Service.</p>"""
    ou: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory organizational unit for the DB instance or cluster.</p>"""
    auth_secret_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the Secrets Manager secret with the credentials for the user that's a member of the domain.</p>"""
    dns_ips: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The IPv4 DNS IP addresses of the primary and secondary Active Directory domain controllers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "domain" in value:
        pairs.append((f"{key_prefix}Domain", str(value["domain"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "fqdn" in value:
        pairs.append((f"{key_prefix}FQDN", str(value["fqdn"])))
    if "iam_role_name" in value:
        pairs.append((f"{key_prefix}IAMRoleName", str(value["iam_role_name"])))
    if "ou" in value:
        pairs.append((f"{key_prefix}OU", str(value["ou"])))
    if "auth_secret_arn" in value:
        pairs.append((f"{key_prefix}AuthSecretArn", str(value["auth_secret_arn"])))
    if "dns_ips" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["dns_ips"], pairs, f"{key_prefix}DnsIps"
        )


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
    child_ou = el.find("OU")
    if child_ou is not None:
        out["ou"] = str(child_ou.text or "")
    child_auth_secret_arn = el.find("AuthSecretArn")
    if child_auth_secret_arn is not None:
        out["auth_secret_arn"] = str(child_auth_secret_arn.text or "")
    child_dns_ips = el.find("DnsIps")
    if child_dns_ips is not None:
        import capo_rds.types.string_list

        out["dns_ips"] = capo_rds.types.string_list.deserialize_query(child_dns_ips)
    return out
