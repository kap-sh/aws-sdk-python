"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CancelElasticsearchServiceSoftwareUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name


class CancelElasticsearchServiceSoftwareUpdateRequest(TypedDict):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the domain that you want to stop the latest service software update on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelElasticsearchServiceSoftwareUpdateRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> CancelElasticsearchServiceSoftwareUpdateRequest:
    out: CancelElasticsearchServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "CancelElasticsearchServiceSoftwareUpdateRequest.domain_name required"
        )
    return out
