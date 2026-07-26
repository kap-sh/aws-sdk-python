"""Generated from Smithy shape ``com.amazonaws.amp#ScraperDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.destination
    import capo_amp.types.iam_role_arn
    import capo_amp.types.role_configuration
    import capo_amp.types.scrape_configuration
    import capo_amp.types.scraper_alias
    import capo_amp.types.scraper_arn
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_status
    import capo_amp.types.source
    import capo_amp.types.status_reason
    import capo_amp.types.tag_map


class ScraperDescription(TypedDict, closed=True):
    alias: NotRequired["capo_amp.types.scraper_alias.ScraperAlias"]
    """<p>(Optional) A name associated with the scraper.</p>"""
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper. For example, <code>s-example1-1234-abcd-5678-ef9012abcd34</code>.</p>"""
    arn: "capo_amp.types.scraper_arn.ScraperArn"
    """<p>The Amazon Resource Name (ARN) of the scraper. For example, <code>arn:aws:aps:&lt;region&gt;:123456798012:scraper/s-example1-1234-abcd-5678-ef9012abcd34</code>.</p>"""
    role_arn: "capo_amp.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.</p> <p>For example, <code>arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-12example</code>.</p>"""
    status: "capo_amp.types.scraper_status.ScraperStatus"
    """<p>A structure that contains the current status of the scraper.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the scraper was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The date and time that the scraper was last modified.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>(Optional) The list of tag keys and values associated with the scraper.</p>"""
    status_reason: NotRequired["capo_amp.types.status_reason.StatusReason"]
    """<p>If there is a failure, the reason for the failure.</p>"""
    scrape_configuration: "capo_amp.types.scrape_configuration.ScrapeConfiguration"
    """<p>The configuration in use by the scraper.</p>"""
    source: "capo_amp.types.source.Source"
    """<p>The Amazon EKS cluster from which the scraper collects metrics.</p>"""
    destination: "capo_amp.types.destination.Destination"
    """<p>The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.</p>"""
    role_configuration: NotRequired[
        "capo_amp.types.role_configuration.RoleConfiguration"
    ]
    """<p>This structure displays information about the IAM roles used for cross-account scraping configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperDescription) -> dict:
    out: dict = {}
    if "alias" in value:
        out["alias"] = value["alias"]
    out["scraperId"] = value["scraper_id"]
    out["arn"] = value["arn"]
    out["roleArn"] = value["role_arn"]
    import capo_amp.types.scraper_status

    out["status"] = capo_amp.types.scraper_status.serialize_json(value["status"])
    import capo_amp.types._prelude.timestamp

    out["createdAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_amp.types._prelude.timestamp

    out["lastModifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["last_modified_at"]
    )
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
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
    return out


def deserialize_json(data: dict) -> ScraperDescription:
    out: ScraperDescription = {}  # type: ignore[typeddict-item]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "scraperId" in data:
        out["scraper_id"] = data["scraperId"]
    else:
        raise DeserializationError("ScraperDescription.scraper_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ScraperDescription.arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ScraperDescription.role_arn required")
    if "status" in data:
        import capo_amp.types.scraper_status

        out["status"] = capo_amp.types.scraper_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("ScraperDescription.status required")
    if "createdAt" in data:
        import capo_amp.types._prelude.timestamp

        out["created_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ScraperDescription.created_at required")
    if "lastModifiedAt" in data:
        import capo_amp.types._prelude.timestamp

        out["last_modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["lastModifiedAt"]
        )
    else:
        raise DeserializationError("ScraperDescription.last_modified_at required")
    if "tags" in data:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "scrapeConfiguration" in data:
        import capo_amp.types.scrape_configuration

        out["scrape_configuration"] = (
            capo_amp.types.scrape_configuration.deserialize_json(
                data["scrapeConfiguration"]
            )
        )
    else:
        raise DeserializationError("ScraperDescription.scrape_configuration required")
    if "source" in data:
        import capo_amp.types.source

        out["source"] = capo_amp.types.source.deserialize_json(data["source"])
    else:
        raise DeserializationError("ScraperDescription.source required")
    if "destination" in data:
        import capo_amp.types.destination

        out["destination"] = capo_amp.types.destination.deserialize_json(
            data["destination"]
        )
    else:
        raise DeserializationError("ScraperDescription.destination required")
    if "roleConfiguration" in data:
        import capo_amp.types.role_configuration

        out["role_configuration"] = capo_amp.types.role_configuration.deserialize_json(
            data["roleConfiguration"]
        )
    return out
