"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DomainStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.arn
    import aws_sdk_cloudsearch.types.boolean
    import aws_sdk_cloudsearch.types.domain_id
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.instance_count
    import aws_sdk_cloudsearch.types.limits
    import aws_sdk_cloudsearch.types.partition_count
    import aws_sdk_cloudsearch.types.search_instance_type
    import aws_sdk_cloudsearch.types.service_endpoint


class DomainStatus(TypedDict, closed=True):
    domain_id: "aws_sdk_cloudsearch.types.domain_id.DomainId"
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    arn: NotRequired["aws_sdk_cloudsearch.types.arn.ARN"]
    created: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>True if the search domain is created. It can take several minutes to initialize a domain when <a>CreateDomain</a> is called. Newly created search domains are returned from <a>DescribeDomains</a> with a false value for Created until domain creation is complete.</p>"""
    deleted: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>True if the search domain has been deleted. The system must clean up resources dedicated to the search domain when <a>DeleteDomain</a> is called. Newly deleted search domains are returned from <a>DescribeDomains</a> with a true value for IsDeleted for several minutes until resource cleanup is complete.</p>"""
    doc_service: NotRequired[
        "aws_sdk_cloudsearch.types.service_endpoint.ServiceEndpoint"
    ]
    """<p>The service endpoint for updating documents in a search domain.</p>"""
    search_service: NotRequired[
        "aws_sdk_cloudsearch.types.service_endpoint.ServiceEndpoint"
    ]
    """<p>The service endpoint for requesting search results from a search domain.</p>"""
    requires_index_documents: "aws_sdk_cloudsearch.types.boolean.Boolean"
    """<p>True if <a>IndexDocuments</a> needs to be called to activate the current domain configuration.</p>"""
    processing: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>True if processing is being done to activate the current domain configuration.</p>"""
    search_instance_type: NotRequired[
        "aws_sdk_cloudsearch.types.search_instance_type.SearchInstanceType"
    ]
    """<p>The instance type that is being used to process search requests.</p>"""
    search_partition_count: NotRequired[
        "aws_sdk_cloudsearch.types.partition_count.PartitionCount"
    ]
    """<p>The number of partitions across which the search index is spread.</p>"""
    search_instance_count: NotRequired[
        "aws_sdk_cloudsearch.types.instance_count.InstanceCount"
    ]
    """<p>The number of search instances that are available to process search requests.</p>"""
    limits: NotRequired["aws_sdk_cloudsearch.types.limits.Limits"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainId", str(value["domain_id"])))
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    if "arn" in value:
        pairs.append((f"{prefix}.ARN", str(value["arn"])))
    if "created" in value:
        pairs.append((f"{prefix}.Created", "true" if value["created"] else "false"))
    if "deleted" in value:
        pairs.append((f"{prefix}.Deleted", "true" if value["deleted"] else "false"))
    if "doc_service" in value:
        import aws_sdk_cloudsearch.types.service_endpoint

        aws_sdk_cloudsearch.types.service_endpoint.serialize_query(
            value["doc_service"], pairs, f"{prefix}.DocService"
        )
    if "search_service" in value:
        import aws_sdk_cloudsearch.types.service_endpoint

        aws_sdk_cloudsearch.types.service_endpoint.serialize_query(
            value["search_service"], pairs, f"{prefix}.SearchService"
        )
    pairs.append(
        (
            f"{prefix}.RequiresIndexDocuments",
            "true" if value["requires_index_documents"] else "false",
        )
    )
    if "processing" in value:
        pairs.append(
            (f"{prefix}.Processing", "true" if value["processing"] else "false")
        )
    if "search_instance_type" in value:
        pairs.append(
            (f"{prefix}.SearchInstanceType", str(value["search_instance_type"]))
        )
    if "search_partition_count" in value:
        pairs.append(
            (f"{prefix}.SearchPartitionCount", str(value["search_partition_count"]))
        )
    if "search_instance_count" in value:
        pairs.append(
            (f"{prefix}.SearchInstanceCount", str(value["search_instance_count"]))
        )
    if "limits" in value:
        import aws_sdk_cloudsearch.types.limits

        aws_sdk_cloudsearch.types.limits.serialize_query(
            value["limits"], pairs, f"{prefix}.Limits"
        )


def deserialize_query(el: Element) -> DomainStatus:
    out: DomainStatus = {}  # type: ignore[typeddict-item]
    child_domain_id = el.find("DomainId")
    if child_domain_id is not None:
        out["domain_id"] = str(child_domain_id.text or "")
    else:
        raise DeserializationError("DomainStatus.domain_id required")
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DomainStatus.domain_name required")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_created = el.find("Created")
    if child_created is not None:
        out["created"] = (child_created.text or "").lower() == "true"
    child_deleted = el.find("Deleted")
    if child_deleted is not None:
        out["deleted"] = (child_deleted.text or "").lower() == "true"
    child_doc_service = el.find("DocService")
    if child_doc_service is not None:
        import aws_sdk_cloudsearch.types.service_endpoint

        out["doc_service"] = (
            aws_sdk_cloudsearch.types.service_endpoint.deserialize_query(
                child_doc_service
            )
        )
    child_search_service = el.find("SearchService")
    if child_search_service is not None:
        import aws_sdk_cloudsearch.types.service_endpoint

        out["search_service"] = (
            aws_sdk_cloudsearch.types.service_endpoint.deserialize_query(
                child_search_service
            )
        )
    child_requires_index_documents = el.find("RequiresIndexDocuments")
    if child_requires_index_documents is not None:
        out["requires_index_documents"] = (
            child_requires_index_documents.text or ""
        ).lower() == "true"
    else:
        raise DeserializationError("DomainStatus.requires_index_documents required")
    child_processing = el.find("Processing")
    if child_processing is not None:
        out["processing"] = (child_processing.text or "").lower() == "true"
    child_search_instance_type = el.find("SearchInstanceType")
    if child_search_instance_type is not None:
        out["search_instance_type"] = str(child_search_instance_type.text or "")
    child_search_partition_count = el.find("SearchPartitionCount")
    if child_search_partition_count is not None:
        out["search_partition_count"] = int(child_search_partition_count.text or "")
    child_search_instance_count = el.find("SearchInstanceCount")
    if child_search_instance_count is not None:
        out["search_instance_count"] = int(child_search_instance_count.text or "")
    child_limits = el.find("Limits")
    if child_limits is not None:
        import aws_sdk_cloudsearch.types.limits

        out["limits"] = aws_sdk_cloudsearch.types.limits.deserialize_query(child_limits)
    return out
