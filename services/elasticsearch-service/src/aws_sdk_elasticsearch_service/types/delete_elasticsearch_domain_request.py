"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeleteElasticsearchDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name


class DeleteElasticsearchDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the Elasticsearch domain that you want to permanently delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteElasticsearchDomainRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteElasticsearchDomainRequest:
    out: DeleteElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
    return out
