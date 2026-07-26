"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreRevocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.number_of_revoked_entries
    import capo_elastic_load_balancing_v2.types.revocation_id
    import capo_elastic_load_balancing_v2.types.revocation_type
    import capo_elastic_load_balancing_v2.types.trust_store_arn


class TrustStoreRevocation(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    revocation_id: NotRequired[
        "capo_elastic_load_balancing_v2.types.revocation_id.RevocationId"
    ]
    """<p>The revocation ID of the revocation file.</p>"""
    revocation_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.revocation_type.RevocationType"
    ]
    """<p>The type of revocation file.</p>"""
    number_of_revoked_entries: NotRequired[
        "capo_elastic_load_balancing_v2.types.number_of_revoked_entries.NumberOfRevokedEntries"
    ]
    """<p>The number of revoked certificates.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStoreRevocation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "trust_store_arn" in value:
        pairs.append((f"{prefix}.TrustStoreArn", str(value["trust_store_arn"])))
    if "revocation_id" in value:
        pairs.append((f"{prefix}.RevocationId", str(value["revocation_id"])))
    if "revocation_type" in value:
        import capo_elastic_load_balancing_v2.types.revocation_type

        capo_elastic_load_balancing_v2.types.revocation_type.serialize_query(
            value["revocation_type"], pairs, f"{prefix}.RevocationType"
        )
    if "number_of_revoked_entries" in value:
        pairs.append(
            (
                f"{prefix}.NumberOfRevokedEntries",
                str(value["number_of_revoked_entries"]),
            )
        )


def deserialize_query(el: Element) -> TrustStoreRevocation:
    out: TrustStoreRevocation = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_revocation_id = el.find("RevocationId")
    if child_revocation_id is not None:
        out["revocation_id"] = int(child_revocation_id.text or "")
    child_revocation_type = el.find("RevocationType")
    if child_revocation_type is not None:
        import capo_elastic_load_balancing_v2.types.revocation_type

        out["revocation_type"] = (
            capo_elastic_load_balancing_v2.types.revocation_type.deserialize_query(
                child_revocation_type
            )
        )
    child_number_of_revoked_entries = el.find("NumberOfRevokedEntries")
    if child_number_of_revoked_entries is not None:
        out["number_of_revoked_entries"] = int(
            child_number_of_revoked_entries.text or ""
        )
    return out
