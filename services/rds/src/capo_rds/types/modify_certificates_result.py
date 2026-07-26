"""Generated from Smithy shape ``com.amazonaws.rds#ModifyCertificatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.certificate


class ModifyCertificatesResult(TypedDict, closed=True):
    certificate: NotRequired["capo_rds.types.certificate.Certificate"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCertificatesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificate" in value:
        import capo_rds.types.certificate

        capo_rds.types.certificate.serialize_query(
            value["certificate"], pairs, f"{prefix}.Certificate"
        )


def deserialize_query(el: Element) -> ModifyCertificatesResult:
    out: ModifyCertificatesResult = {}  # type: ignore[typeddict-item]
    child_certificate = el.find("Certificate")
    if child_certificate is not None:
        import capo_rds.types.certificate

        out["certificate"] = capo_rds.types.certificate.deserialize_query(
            child_certificate
        )
    return out
