"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.elasticsearch_domain_status_list


class DescribeElasticsearchDomainsResponse(TypedDict, closed=True):
    domain_status_list: "aws_sdk_elasticsearch_service.types.elasticsearch_domain_status_list.ElasticsearchDomainStatusList"
    """<p>The status of the domains requested in the <code>DescribeElasticsearchDomains</code> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchDomainsResponse) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.elasticsearch_domain_status_list

    out["DomainStatusList"] = (
        aws_sdk_elasticsearch_service.types.elasticsearch_domain_status_list.serialize_json(
            value["domain_status_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchDomainsResponse:
    out: DescribeElasticsearchDomainsResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatusList" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_domain_status_list

        out["domain_status_list"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_domain_status_list.deserialize_json(
                data["DomainStatusList"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeElasticsearchDomainsResponse.domain_status_list required"
        )
    return out
