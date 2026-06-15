"""Generated from Smithy shape ``com.amazonaws.amp#UpdateScraperRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amp.types.destination
    import aws_sdk_amp.types.idempotency_token
    import aws_sdk_amp.types.role_configuration
    import aws_sdk_amp.types.scrape_configuration
    import aws_sdk_amp.types.scraper_alias
    import aws_sdk_amp.types.scraper_id


class UpdateScraperRequest(TypedDict):
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper to update.</p>"""
    alias: NotRequired["aws_sdk_amp.types.scraper_alias.ScraperAlias"]
    """<p>The new alias of the scraper.</p>"""
    scrape_configuration: NotRequired[
        "aws_sdk_amp.types.scrape_configuration.ScrapeConfiguration"
    ]
    r"""<p>Contains the base-64 encoded YAML configuration for the scraper.</p> <note> <p>For more information about configuring a scraper, see <a href=\"https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html\">Using an Amazon Web Services managed collector</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p> </note>"""
    destination: NotRequired["aws_sdk_amp.types.destination.Destination"]
    """<p>The new Amazon Managed Service for Prometheus workspace to send metrics to.</p>"""
    role_configuration: NotRequired[
        "aws_sdk_amp.types.role_configuration.RoleConfiguration"
    ]
    """<p>Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.</p>"""
    client_token: NotRequired["aws_sdk_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScraperRequest) -> dict:
    out: dict = {}
    if "alias" in value:
        out["alias"] = value["alias"]
    if "scrape_configuration" in value:
        import aws_sdk_amp.types.scrape_configuration

        out["scrapeConfiguration"] = (
            aws_sdk_amp.types.scrape_configuration.serialize_json(
                value["scrape_configuration"]
            )
        )
    if "destination" in value:
        import aws_sdk_amp.types.destination

        out["destination"] = aws_sdk_amp.types.destination.serialize_json(
            value["destination"]
        )
    if "role_configuration" in value:
        import aws_sdk_amp.types.role_configuration

        out["roleConfiguration"] = aws_sdk_amp.types.role_configuration.serialize_json(
            value["role_configuration"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateScraperRequest:
    out: UpdateScraperRequest = {}  # type: ignore[typeddict-item]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "scrapeConfiguration" in data:
        import aws_sdk_amp.types.scrape_configuration

        out["scrape_configuration"] = (
            aws_sdk_amp.types.scrape_configuration.deserialize_json(
                data["scrapeConfiguration"]
            )
        )
    if "destination" in data:
        import aws_sdk_amp.types.destination

        out["destination"] = aws_sdk_amp.types.destination.deserialize_json(
            data["destination"]
        )
    if "roleConfiguration" in data:
        import aws_sdk_amp.types.role_configuration

        out["role_configuration"] = (
            aws_sdk_amp.types.role_configuration.deserialize_json(
                data["roleConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
