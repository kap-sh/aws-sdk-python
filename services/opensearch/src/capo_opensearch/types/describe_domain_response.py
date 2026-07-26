"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.domain_status


class DescribeDomainResponse(TypedDict, closed=True):
    domain_status: "capo_opensearch.types.domain_status.DomainStatus"
    """<p>List that contains the status of each specified OpenSearch Service domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.domain_status

    out["DomainStatus"] = capo_opensearch.types.domain_status.serialize_json(
        value["domain_status"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDomainResponse:
    out: DescribeDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatus" in data:
        import capo_opensearch.types.domain_status

        out["domain_status"] = capo_opensearch.types.domain_status.deserialize_json(
            data["DomainStatus"]
        )
    else:
        raise DeserializationError("DescribeDomainResponse.domain_status required")
    return out
