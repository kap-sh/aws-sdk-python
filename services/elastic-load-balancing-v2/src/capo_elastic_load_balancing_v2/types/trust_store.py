"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.number_of_ca_certificates
    import capo_elastic_load_balancing_v2.types.total_revoked_entries
    import capo_elastic_load_balancing_v2.types.trust_store_arn
    import capo_elastic_load_balancing_v2.types.trust_store_name
    import capo_elastic_load_balancing_v2.types.trust_store_status


class TrustStore(TypedDict, closed=True):
    name: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_name.TrustStoreName"
    ]
    """<p>The name of the trust store.</p>"""
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    status: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_status.TrustStoreStatus"
    ]
    """<p>The current status of the trust store.</p>"""
    number_of_ca_certificates: NotRequired[
        "capo_elastic_load_balancing_v2.types.number_of_ca_certificates.NumberOfCaCertificates"
    ]
    """<p>The number of ca certificates in the trust store.</p>"""
    total_revoked_entries: NotRequired[
        "capo_elastic_load_balancing_v2.types.total_revoked_entries.TotalRevokedEntries"
    ]
    """<p>The number of revoked certificates in the trust store.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStore, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "trust_store_arn" in value:
        pairs.append((f"{key_prefix}TrustStoreArn", str(value["trust_store_arn"])))
    if "status" in value:
        import capo_elastic_load_balancing_v2.types.trust_store_status

        capo_elastic_load_balancing_v2.types.trust_store_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "number_of_ca_certificates" in value:
        pairs.append(
            (
                f"{key_prefix}NumberOfCaCertificates",
                str(value["number_of_ca_certificates"]),
            )
        )
    if "total_revoked_entries" in value:
        pairs.append(
            (f"{key_prefix}TotalRevokedEntries", str(value["total_revoked_entries"]))
        )


def deserialize_query(el: Element) -> TrustStore:
    out: TrustStore = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_elastic_load_balancing_v2.types.trust_store_status

        out["status"] = (
            capo_elastic_load_balancing_v2.types.trust_store_status.deserialize_query(
                child_status
            )
        )
    child_number_of_ca_certificates = el.find("NumberOfCaCertificates")
    if child_number_of_ca_certificates is not None:
        out["number_of_ca_certificates"] = int(
            child_number_of_ca_certificates.text or ""
        )
    child_total_revoked_entries = el.find("TotalRevokedEntries")
    if child_total_revoked_entries is not None:
        out["total_revoked_entries"] = int(child_total_revoked_entries.text or "")
    return out
