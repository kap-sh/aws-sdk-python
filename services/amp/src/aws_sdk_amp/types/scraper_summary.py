"""Generated from Smithy shape ``com.amazonaws.amp#ScraperSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_amp.types.destination
    import aws_sdk_amp.types.iam_role_arn
    import aws_sdk_amp.types.role_configuration
    import aws_sdk_amp.types.scraper_alias
    import aws_sdk_amp.types.scraper_arn
    import aws_sdk_amp.types.scraper_id
    import aws_sdk_amp.types.scraper_status
    import aws_sdk_amp.types.source
    import aws_sdk_amp.types.status_reason
    import aws_sdk_amp.types.tag_map


class ScraperSummary(TypedDict):
    alias: NotRequired["aws_sdk_amp.types.scraper_alias.ScraperAlias"]
    """<p>(Optional) A name associated with the scraper.</p>"""
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper.</p>"""
    arn: "aws_sdk_amp.types.scraper_arn.ScraperArn"
    """<p>The Amazon Resource Name (ARN) of the scraper.</p>"""
    role_arn: "aws_sdk_amp.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.</p>"""
    status: "aws_sdk_amp.types.scraper_status.ScraperStatus"
    """<p>A structure that contains the current status of the scraper.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the scraper was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The date and time that the scraper was last modified.</p>"""
    tags: NotRequired["aws_sdk_amp.types.tag_map.TagMap"]
    """<p>(Optional) The list of tag keys and values associated with the scraper.</p>"""
    status_reason: NotRequired["aws_sdk_amp.types.status_reason.StatusReason"]
    """<p>If there is a failure, the reason for the failure.</p>"""
    source: "aws_sdk_amp.types.source.Source"
    """<p>The Amazon EKS cluster from which the scraper collects metrics.</p>"""
    destination: "aws_sdk_amp.types.destination.Destination"
    """<p>The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.</p>"""
    role_configuration: NotRequired[
        "aws_sdk_amp.types.role_configuration.RoleConfiguration"
    ]
    """<p>This structure displays information about the IAM roles used for cross-account scraping configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperSummary) -> dict:
    out: dict = {}
    if "alias" in value:
        out["alias"] = value["alias"]
    out["scraperId"] = value["scraper_id"]
    out["arn"] = value["arn"]
    out["roleArn"] = value["role_arn"]
    import aws_sdk_amp.types.scraper_status

    out["status"] = aws_sdk_amp.types.scraper_status.serialize_json(value["status"])
    import aws_sdk_amp.types._prelude.timestamp

    out["createdAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["lastModifiedAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["last_modified_at"]
    )
    if "tags" in value:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_amp.types.source

    out["source"] = aws_sdk_amp.types.source.serialize_json(value["source"])
    import aws_sdk_amp.types.destination

    out["destination"] = aws_sdk_amp.types.destination.serialize_json(
        value["destination"]
    )
    if "role_configuration" in value:
        import aws_sdk_amp.types.role_configuration

        out["roleConfiguration"] = aws_sdk_amp.types.role_configuration.serialize_json(
            value["role_configuration"]
        )
    return out


def deserialize_json(data: dict) -> ScraperSummary:
    out: ScraperSummary = {}  # type: ignore[typeddict-item]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "scraperId" in data:
        out["scraper_id"] = data["scraperId"]
    else:
        raise DeserializationError("ScraperSummary.scraper_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ScraperSummary.arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ScraperSummary.role_arn required")
    if "status" in data:
        import aws_sdk_amp.types.scraper_status

        out["status"] = aws_sdk_amp.types.scraper_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ScraperSummary.status required")
    if "createdAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["created_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ScraperSummary.created_at required")
    if "lastModifiedAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["last_modified_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["lastModifiedAt"]
        )
    else:
        raise DeserializationError("ScraperSummary.last_modified_at required")
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "source" in data:
        import aws_sdk_amp.types.source

        out["source"] = aws_sdk_amp.types.source.deserialize_json(data["source"])
    else:
        raise DeserializationError("ScraperSummary.source required")
    if "destination" in data:
        import aws_sdk_amp.types.destination

        out["destination"] = aws_sdk_amp.types.destination.deserialize_json(
            data["destination"]
        )
    else:
        raise DeserializationError("ScraperSummary.destination required")
    if "roleConfiguration" in data:
        import aws_sdk_amp.types.role_configuration

        out["role_configuration"] = (
            aws_sdk_amp.types.role_configuration.deserialize_json(
                data["roleConfiguration"]
            )
        )
    return out
