"""Generated from Smithy shape ``com.amazonaws.amp#CreateScraperRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.destination
    import capo_amp.types.idempotency_token
    import capo_amp.types.role_configuration
    import capo_amp.types.scrape_configuration
    import capo_amp.types.scraper_alias
    import capo_amp.types.source
    import capo_amp.types.tag_map


class CreateScraperRequest(TypedDict, closed=True):
    alias: NotRequired["capo_amp.types.scraper_alias.ScraperAlias"]
    """<p>(optional) An alias to associate with the scraper. This is for your use, and does not need to be unique.</p>"""
    scrape_configuration: "capo_amp.types.scrape_configuration.ScrapeConfiguration"
    r"""<p>The configuration file to use in the new scraper. For more information, see <a href=\"https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration\">Scraper configuration</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>"""
    source: "capo_amp.types.source.Source"
    """<p>The Amazon EKS or Amazon Web Services cluster from which the scraper will collect metrics.</p>"""
    destination: "capo_amp.types.destination.Destination"
    """<p>The Amazon Managed Service for Prometheus workspace to send metrics to.</p>"""
    role_configuration: NotRequired[
        "capo_amp.types.role_configuration.RoleConfiguration"
    ]
    """<p>Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>(Optional) The list of tag keys and values to associate with the scraper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScraperRequest) -> dict:
    out: dict = {}
    if "alias" in value:
        out["alias"] = value["alias"]
    import capo_amp.types.scrape_configuration

    out["scrapeConfiguration"] = capo_amp.types.scrape_configuration.serialize_json(
        value["scrape_configuration"]
    )
    import capo_amp.types.source

    out["source"] = capo_amp.types.source.serialize_json(value["source"])
    import capo_amp.types.destination

    out["destination"] = capo_amp.types.destination.serialize_json(value["destination"])
    if "role_configuration" in value:
        import capo_amp.types.role_configuration

        out["roleConfiguration"] = capo_amp.types.role_configuration.serialize_json(
            value["role_configuration"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateScraperRequest:
    out: CreateScraperRequest = {}  # type: ignore[typeddict-item]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "scrapeConfiguration" in data:
        import capo_amp.types.scrape_configuration

        out["scrape_configuration"] = (
            capo_amp.types.scrape_configuration.deserialize_json(
                data["scrapeConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateScraperRequest.scrape_configuration required")
    if "source" in data:
        import capo_amp.types.source

        out["source"] = capo_amp.types.source.deserialize_json(data["source"])
    else:
        raise DeserializationError("CreateScraperRequest.source required")
    if "destination" in data:
        import capo_amp.types.destination

        out["destination"] = capo_amp.types.destination.deserialize_json(
            data["destination"]
        )
    else:
        raise DeserializationError("CreateScraperRequest.destination required")
    if "roleConfiguration" in data:
        import capo_amp.types.role_configuration

        out["role_configuration"] = capo_amp.types.role_configuration.deserialize_json(
            data["roleConfiguration"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
