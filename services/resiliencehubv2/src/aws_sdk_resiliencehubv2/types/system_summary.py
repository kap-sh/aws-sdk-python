"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.organization_id
    import aws_sdk_resiliencehubv2.types.ou_id
    import aws_sdk_resiliencehubv2.types.system_id


class SystemSummary(TypedDict):
    system_id: "aws_sdk_resiliencehubv2.types.system_id.SystemId"
    name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName"
    system_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    user_journeys_count: NotRequired["int"]
    """<p>The number of user journeys in the system.</p>"""
    services_count: NotRequired["int"]
    """<p>The number of services in the system.</p>"""
    organization_id: NotRequired[
        "aws_sdk_resiliencehubv2.types.organization_id.OrganizationId"
    ]
    """<p>Displayed only if caller has access.</p>"""
    ou_id: NotRequired["aws_sdk_resiliencehubv2.types.ou_id.OuId"]
    """<p>Displayed only if caller has access.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemSummary) -> dict:
    out: dict = {}
    out["systemId"] = value["system_id"]
    out["name"] = value["name"]
    if "system_arn" in value:
        out["systemArn"] = value["system_arn"]
    if "user_journeys_count" in value:
        out["userJourneysCount"] = value["user_journeys_count"]
    if "services_count" in value:
        out["servicesCount"] = value["services_count"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "ou_id" in value:
        out["ouId"] = value["ou_id"]
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemSummary:
    out: SystemSummary = {}  # type: ignore[typeddict-item]
    if "systemId" in data:
        out["system_id"] = data["systemId"]
    else:
        raise DeserializationError("SystemSummary.system_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SystemSummary.name required")
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    if "userJourneysCount" in data:
        out["user_journeys_count"] = data["userJourneysCount"]
    if "servicesCount" in data:
        out["services_count"] = data["servicesCount"]
    if "organizationId" in data:
        out["organization_id"] = data["organizationId"]
    if "ouId" in data:
        out["ou_id"] = data["ouId"]
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
