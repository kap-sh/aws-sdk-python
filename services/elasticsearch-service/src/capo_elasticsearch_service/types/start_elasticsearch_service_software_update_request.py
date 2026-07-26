"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#StartElasticsearchServiceSoftwareUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name


class StartElasticsearchServiceSoftwareUpdateRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the domain that you want to update to the latest service software.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartElasticsearchServiceSoftwareUpdateRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> StartElasticsearchServiceSoftwareUpdateRequest:
    out: StartElasticsearchServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "StartElasticsearchServiceSoftwareUpdateRequest.domain_name required"
        )
    return out
