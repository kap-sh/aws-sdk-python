"""Generated from Smithy shape ``com.amazonaws.datazone#DomainSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.domain_description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_name
    import aws_sdk_datazone.types.domain_status
    import aws_sdk_datazone.types.domain_version
    import aws_sdk_datazone.types.updated_at


class DomainSummary(TypedDict):
    id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    name: "aws_sdk_datazone.types.domain_name.DomainName"
    """<p>A name of an Amazon DataZone domain.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.domain_description.DomainDescription"
    ]
    """<p>A description of an Amazon DataZone domain.</p>"""
    arn: "str"
    """<p>The ARN of the Amazon DataZone domain.</p>"""
    managed_account_id: "str"
    """<p>The identifier of the Amazon Web Services account that manages the domain.</p>"""
    status: "aws_sdk_datazone.types.domain_status.DomainStatus"
    """<p>The status of the Amazon DataZone domain.</p>"""
    portal_url: NotRequired["str"]
    """<p>The data portal URL for the Amazon DataZone domain.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>A timestamp of when a Amazon DataZone domain was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>A timestamp of when a Amazon DataZone domain was last updated.</p>"""
    domain_version: NotRequired["aws_sdk_datazone.types.domain_version.DomainVersion"]
    """<p>The domain version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    out["managedAccountId"] = value["managed_account_id"]
    import aws_sdk_datazone.types.domain_status

    out["status"] = aws_sdk_datazone.types.domain_status.serialize_json(value["status"])
    if "portal_url" in value:
        out["portalUrl"] = value["portal_url"]
    import aws_sdk_datazone.types.created_at

    out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    if "last_updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["lastUpdatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["last_updated_at"]
        )
    if "domain_version" in value:
        import aws_sdk_datazone.types.domain_version

        out["domainVersion"] = aws_sdk_datazone.types.domain_version.serialize_json(
            value["domain_version"]
        )
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DomainSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DomainSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DomainSummary.arn required")
    if "managedAccountId" in data:
        out["managed_account_id"] = data["managedAccountId"]
    else:
        raise DeserializationError("DomainSummary.managed_account_id required")
    if "status" in data:
        import aws_sdk_datazone.types.domain_status

        out["status"] = aws_sdk_datazone.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DomainSummary.status required")
    if "portalUrl" in data:
        out["portal_url"] = data["portalUrl"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("DomainSummary.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["last_updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "domainVersion" in data:
        import aws_sdk_datazone.types.domain_version

        out["domain_version"] = aws_sdk_datazone.types.domain_version.deserialize_json(
            data["domainVersion"]
        )
    return out
