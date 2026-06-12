"""Generated from Smithy shape ``com.amazonaws.marketplacereporting#GetBuyerDashboardInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_reporting.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_reporting.types.dashboard_identifier
    import aws_sdk_marketplace_reporting.types.embedding_domains


class GetBuyerDashboardInput(TypedDict):
    dashboard_identifier: (
        "aws_sdk_marketplace_reporting.types.dashboard_identifier.DashboardIdentifier"
    )
    """<p>The ARN of the requested dashboard.</p>"""
    embedding_domains: (
        "aws_sdk_marketplace_reporting.types.embedding_domains.EmbeddingDomains"
    )
    """<p>Fully qualified domains that you add to the allow list for access to the generated URL that is then embedded. You can list up to two domains or subdomains in each API call. To include all subdomains under a specific domain, use <code>*</code>. For example, <code>https://*.amazon.com</code> includes all subdomains under <code>https://aws.amazon.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuyerDashboardInput) -> dict:
    out: dict = {}
    out["dashboardIdentifier"] = value["dashboard_identifier"]
    import aws_sdk_marketplace_reporting.types.embedding_domains

    out["embeddingDomains"] = (
        aws_sdk_marketplace_reporting.types.embedding_domains.serialize_json(
            value["embedding_domains"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBuyerDashboardInput:
    out: GetBuyerDashboardInput = {}  # type: ignore[typeddict-item]
    if "dashboardIdentifier" in data:
        out["dashboard_identifier"] = data["dashboardIdentifier"]
    else:
        raise DeserializationError(
            "GetBuyerDashboardInput.dashboard_identifier required"
        )
    if "embeddingDomains" in data:
        import aws_sdk_marketplace_reporting.types.embedding_domains

        out["embedding_domains"] = (
            aws_sdk_marketplace_reporting.types.embedding_domains.deserialize_json(
                data["embeddingDomains"]
            )
        )
    else:
        raise DeserializationError("GetBuyerDashboardInput.embedding_domains required")
    return out
