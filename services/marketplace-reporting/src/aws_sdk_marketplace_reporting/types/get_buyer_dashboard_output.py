"""Generated from Smithy shape ``com.amazonaws.marketplacereporting#GetBuyerDashboardOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_reporting.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_reporting.types.dashboard_identifier
    import aws_sdk_marketplace_reporting.types.embedding_domains


class GetBuyerDashboardOutput(TypedDict, closed=True):
    embed_url: "str"
    """<p>The dashboard's embedding URL.</p>"""
    dashboard_identifier: (
        "aws_sdk_marketplace_reporting.types.dashboard_identifier.DashboardIdentifier"
    )
    """<p>The ARN of the returned dashboard.</p>"""
    embedding_domains: (
        "aws_sdk_marketplace_reporting.types.embedding_domains.EmbeddingDomains"
    )
    """<p>The fully qualified domains specified in the request. The domains enable access to the generated URL that is then embedded. You can list up to two domains or subdomains in each API call. To include all subdomains under a specific domain, use <code>*</code>. For example, <code>https://*.amazon.com</code> includes all subdomains under <code>https://aws.amazon.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuyerDashboardOutput) -> dict:
    out: dict = {}
    out["embedUrl"] = value["embed_url"]
    out["dashboardIdentifier"] = value["dashboard_identifier"]
    import aws_sdk_marketplace_reporting.types.embedding_domains

    out["embeddingDomains"] = (
        aws_sdk_marketplace_reporting.types.embedding_domains.serialize_json(
            value["embedding_domains"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBuyerDashboardOutput:
    out: GetBuyerDashboardOutput = {}  # type: ignore[typeddict-item]
    if "embedUrl" in data:
        out["embed_url"] = data["embedUrl"]
    else:
        raise DeserializationError("GetBuyerDashboardOutput.embed_url required")
    if "dashboardIdentifier" in data:
        out["dashboard_identifier"] = data["dashboardIdentifier"]
    else:
        raise DeserializationError(
            "GetBuyerDashboardOutput.dashboard_identifier required"
        )
    if "embeddingDomains" in data:
        import aws_sdk_marketplace_reporting.types.embedding_domains

        out["embedding_domains"] = (
            aws_sdk_marketplace_reporting.types.embedding_domains.deserialize_json(
                data["embeddingDomains"]
            )
        )
    else:
        raise DeserializationError("GetBuyerDashboardOutput.embedding_domains required")
    return out
