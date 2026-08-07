"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_status


class DeleteDomainResponse(TypedDict, closed=True):
    domain_status: NotRequired["capo_cloudsearch.types.domain_status.DomainStatus"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDomainResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "domain_status" in value:
        import capo_cloudsearch.types.domain_status

        capo_cloudsearch.types.domain_status.serialize_query(
            value["domain_status"], pairs, f"{key_prefix}DomainStatus"
        )


def deserialize_query(el: Element) -> DeleteDomainResponse:
    out: DeleteDomainResponse = {}  # type: ignore[typeddict-item]
    child_domain_status = el.find("DomainStatus")
    if child_domain_status is not None:
        import capo_cloudsearch.types.domain_status

        out["domain_status"] = capo_cloudsearch.types.domain_status.deserialize_query(
            child_domain_status
        )
    return out
