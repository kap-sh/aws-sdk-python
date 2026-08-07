"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#MutualAuthenticationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.advertise_trust_store_ca_names_enum
    import capo_elastic_load_balancing_v2.types.ignore_client_certificate_expiry
    import capo_elastic_load_balancing_v2.types.mode
    import capo_elastic_load_balancing_v2.types.trust_store_arn
    import capo_elastic_load_balancing_v2.types.trust_store_association_status_enum


class MutualAuthenticationAttributes(TypedDict, closed=True):
    mode: NotRequired["capo_elastic_load_balancing_v2.types.mode.Mode"]
    """<p>The client certificate handling method. Options are <code>off</code>, <code>passthrough</code> or <code>verify</code>. The default value is <code>off</code>.</p>"""
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    ignore_client_certificate_expiry: NotRequired[
        "capo_elastic_load_balancing_v2.types.ignore_client_certificate_expiry.IgnoreClientCertificateExpiry"
    ]
    """<p>Indicates whether expired client certificates are ignored.</p>"""
    trust_store_association_status: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_association_status_enum.TrustStoreAssociationStatusEnum"
    ]
    """<p>Indicates a shared trust stores association status.</p>"""
    advertise_trust_store_ca_names: NotRequired[
        "capo_elastic_load_balancing_v2.types.advertise_trust_store_ca_names_enum.AdvertiseTrustStoreCaNamesEnum"
    ]
    """<p>Indicates whether trust store CA certificate names are advertised.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MutualAuthenticationAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "mode" in value:
        pairs.append((f"{key_prefix}Mode", str(value["mode"])))
    if "trust_store_arn" in value:
        pairs.append((f"{key_prefix}TrustStoreArn", str(value["trust_store_arn"])))
    if "ignore_client_certificate_expiry" in value:
        pairs.append(
            (
                f"{key_prefix}IgnoreClientCertificateExpiry",
                "true" if value["ignore_client_certificate_expiry"] else "false",
            )
        )
    if "trust_store_association_status" in value:
        import capo_elastic_load_balancing_v2.types.trust_store_association_status_enum

        capo_elastic_load_balancing_v2.types.trust_store_association_status_enum.serialize_query(
            value["trust_store_association_status"],
            pairs,
            f"{key_prefix}TrustStoreAssociationStatus",
        )
    if "advertise_trust_store_ca_names" in value:
        import capo_elastic_load_balancing_v2.types.advertise_trust_store_ca_names_enum

        capo_elastic_load_balancing_v2.types.advertise_trust_store_ca_names_enum.serialize_query(
            value["advertise_trust_store_ca_names"],
            pairs,
            f"{key_prefix}AdvertiseTrustStoreCaNames",
        )


def deserialize_query(el: Element) -> MutualAuthenticationAttributes:
    out: MutualAuthenticationAttributes = {}  # type: ignore[typeddict-item]
    child_mode = el.find("Mode")
    if child_mode is not None:
        out["mode"] = str(child_mode.text or "")
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_ignore_client_certificate_expiry = el.find("IgnoreClientCertificateExpiry")
    if child_ignore_client_certificate_expiry is not None:
        out["ignore_client_certificate_expiry"] = (
            child_ignore_client_certificate_expiry.text or ""
        ).lower() == "true"
    child_trust_store_association_status = el.find("TrustStoreAssociationStatus")
    if child_trust_store_association_status is not None:
        import capo_elastic_load_balancing_v2.types.trust_store_association_status_enum

        out["trust_store_association_status"] = (
            capo_elastic_load_balancing_v2.types.trust_store_association_status_enum.deserialize_query(
                child_trust_store_association_status
            )
        )
    child_advertise_trust_store_ca_names = el.find("AdvertiseTrustStoreCaNames")
    if child_advertise_trust_store_ca_names is not None:
        import capo_elastic_load_balancing_v2.types.advertise_trust_store_ca_names_enum

        out["advertise_trust_store_ca_names"] = (
            capo_elastic_load_balancing_v2.types.advertise_trust_store_ca_names_enum.deserialize_query(
                child_advertise_trust_store_ca_names
            )
        )
    return out
