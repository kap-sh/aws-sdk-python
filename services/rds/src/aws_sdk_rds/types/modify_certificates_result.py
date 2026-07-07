"""Generated from Smithy shape ``com.amazonaws.rds#ModifyCertificatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.certificate


class ModifyCertificatesResult(TypedDict, closed=True):
    certificate: NotRequired["aws_sdk_rds.types.certificate.Certificate"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCertificatesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificate" in value:
        import aws_sdk_rds.types.certificate

        aws_sdk_rds.types.certificate.serialize_query(
            value["certificate"], pairs, f"{prefix}.Certificate"
        )


def deserialize_query(el: Element) -> ModifyCertificatesResult:
    out: ModifyCertificatesResult = {}  # type: ignore[typeddict-item]
    child_certificate = el.find("Certificate")
    if child_certificate is not None:
        import aws_sdk_rds.types.certificate

        out["certificate"] = aws_sdk_rds.types.certificate.deserialize_query(
            child_certificate
        )
    return out
