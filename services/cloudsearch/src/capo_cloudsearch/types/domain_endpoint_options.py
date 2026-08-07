"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DomainEndpointOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.tls_security_policy


class DomainEndpointOptions(TypedDict, closed=True):
    enforce_https: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether the domain is HTTPS only enabled.</p>"""
    tls_security_policy: NotRequired[
        "capo_cloudsearch.types.tls_security_policy.TLSSecurityPolicy"
    ]
    """<p>The minimum required TLS version</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainEndpointOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enforce_https" in value:
        pairs.append(
            (f"{key_prefix}EnforceHTTPS", "true" if value["enforce_https"] else "false")
        )
    if "tls_security_policy" in value:
        import capo_cloudsearch.types.tls_security_policy

        capo_cloudsearch.types.tls_security_policy.serialize_query(
            value["tls_security_policy"], pairs, f"{key_prefix}TLSSecurityPolicy"
        )


def deserialize_query(el: Element) -> DomainEndpointOptions:
    out: DomainEndpointOptions = {}  # type: ignore[typeddict-item]
    child_enforce_https = el.find("EnforceHTTPS")
    if child_enforce_https is not None:
        out["enforce_https"] = (child_enforce_https.text or "").lower() == "true"
    child_tls_security_policy = el.find("TLSSecurityPolicy")
    if child_tls_security_policy is not None:
        import capo_cloudsearch.types.tls_security_policy

        out["tls_security_policy"] = (
            capo_cloudsearch.types.tls_security_policy.deserialize_query(
                child_tls_security_policy
            )
        )
    return out
