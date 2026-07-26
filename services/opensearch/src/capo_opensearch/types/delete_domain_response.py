"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_status


class DeleteDomainResponse(TypedDict, closed=True):
    domain_status: NotRequired["capo_opensearch.types.domain_status.DomainStatus"]
    """<p>The status of the domain being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainResponse) -> dict:
    out: dict = {}
    if "domain_status" in value:
        import capo_opensearch.types.domain_status

        out["DomainStatus"] = capo_opensearch.types.domain_status.serialize_json(
            value["domain_status"]
        )
    return out


def deserialize_json(data: dict) -> DeleteDomainResponse:
    out: DeleteDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatus" in data:
        import capo_opensearch.types.domain_status

        out["domain_status"] = capo_opensearch.types.domain_status.deserialize_json(
            data["DomainStatus"]
        )
    return out
