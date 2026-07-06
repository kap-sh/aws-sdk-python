"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainLogPublishingOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option


class AwsOpenSearchServiceDomainLogPublishingOptionsDetails(TypedDict, closed=True):
    index_slow_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.AwsOpenSearchServiceDomainLogPublishingOption"
    ]
    """<p>Configures the OpenSearch index logs publishing.</p>"""
    search_slow_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.AwsOpenSearchServiceDomainLogPublishingOption"
    ]
    """<p>Configures the OpenSearch search slow log publishing.</p>"""
    audit_logs: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.AwsOpenSearchServiceDomainLogPublishingOption"
    ]
    """<p>Configures the OpenSearch audit logs publishing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsOpenSearchServiceDomainLogPublishingOptionsDetails,
) -> dict:
    out: dict = {}
    if "index_slow_logs" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option

        out["IndexSlowLogs"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.serialize_json(
                value["index_slow_logs"]
            )
        )
    if "search_slow_logs" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option

        out["SearchSlowLogs"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.serialize_json(
                value["search_slow_logs"]
            )
        )
    if "audit_logs" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option

        out["AuditLogs"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.serialize_json(
                value["audit_logs"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsOpenSearchServiceDomainLogPublishingOptionsDetails:
    out: AwsOpenSearchServiceDomainLogPublishingOptionsDetails = {}  # type: ignore[typeddict-item]
    if "IndexSlowLogs" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option

        out["index_slow_logs"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.deserialize_json(
                data["IndexSlowLogs"]
            )
        )
    if "SearchSlowLogs" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option

        out["search_slow_logs"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.deserialize_json(
                data["SearchSlowLogs"]
            )
        )
    if "AuditLogs" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option

        out["audit_logs"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_option.deserialize_json(
                data["AuditLogs"]
            )
        )
    return out
