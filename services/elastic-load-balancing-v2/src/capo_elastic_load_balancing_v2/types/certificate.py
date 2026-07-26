"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.certificate_arn
    import capo_elastic_load_balancing_v2.types.default


class Certificate(TypedDict, closed=True):
    certificate_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.certificate_arn.CertificateArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    is_default: NotRequired["capo_elastic_load_balancing_v2.types.default.Default"]
    """<p>Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Certificate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificate_arn" in value:
        pairs.append((f"{prefix}.CertificateArn", str(value["certificate_arn"])))
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )


def deserialize_query(el: Element) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    return out
