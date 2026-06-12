"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding_details_list
    import aws_sdk_accessanalyzer.types.finding_id
    import aws_sdk_accessanalyzer.types.finding_status
    import aws_sdk_accessanalyzer.types.finding_type
    import aws_sdk_accessanalyzer.types.resource_type
    import aws_sdk_accessanalyzer.types.timestamp
    import aws_sdk_accessanalyzer.types.token


class GetFindingV2Response(TypedDict):
    analyzed_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource-based policy or IAM entity that generated the finding was analyzed.</p>"""
    created_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was created.</p>"""
    error: NotRequired["str"]
    """<p>An error.</p>"""
    id: "aws_sdk_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    resource: NotRequired["str"]
    """<p>The resource that generated the finding.</p>"""
    resource_type: "aws_sdk_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource identified in the finding.</p>"""
    resource_owner_account: "str"
    """<p>Tye Amazon Web Services account ID that owns the resource.</p>"""
    status: "aws_sdk_accessanalyzer.types.finding_status.FindingStatus"
    """<p>The status of the finding.</p>"""
    updated_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was updated.</p>"""
    finding_details: (
        "aws_sdk_accessanalyzer.types.finding_details_list.FindingDetailsList"
    )
    """<p>A localized message that explains the finding and provides guidance on how to address it.</p>"""
    finding_type: NotRequired["aws_sdk_accessanalyzer.types.finding_type.FindingType"]
    """<p>The type of the finding. For external access analyzers, the type is <code>ExternalAccess</code>. For unused access analyzers, the type can be <code>UnusedIAMRole</code>, <code>UnusedIAMUserAccessKey</code>, <code>UnusedIAMUserPassword</code>, or <code>UnusedPermission</code>. For internal access analyzers, the type is <code>InternalAccess</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingV2Response) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.timestamp

    out["analyzedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["analyzed_at"]
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["createdAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    if "error" in value:
        out["error"] = value["error"]
    out["id"] = value["id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "resource" in value:
        out["resource"] = value["resource"]
    out["resourceType"] = value["resource_type"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    out["status"] = value["status"]
    import aws_sdk_accessanalyzer.types.timestamp

    out["updatedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    import aws_sdk_accessanalyzer.types.finding_details_list

    out["findingDetails"] = (
        aws_sdk_accessanalyzer.types.finding_details_list.serialize_json(
            value["finding_details"]
        )
    )
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    return out


def deserialize_json(data: dict) -> GetFindingV2Response:
    out: GetFindingV2Response = {}  # type: ignore[typeddict-item]
    if "analyzedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["analyzed_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["analyzedAt"]
        )
    else:
        raise DeserializationError("GetFindingV2Response.analyzed_at required")
    if "createdAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["created_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetFindingV2Response.created_at required")
    if "error" in data:
        out["error"] = data["error"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetFindingV2Response.id required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("GetFindingV2Response.resource_type required")
    if "resourceOwnerAccount" in data:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        raise DeserializationError(
            "GetFindingV2Response.resource_owner_account required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetFindingV2Response.status required")
    if "updatedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["updated_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetFindingV2Response.updated_at required")
    if "findingDetails" in data:
        import aws_sdk_accessanalyzer.types.finding_details_list

        out["finding_details"] = (
            aws_sdk_accessanalyzer.types.finding_details_list.deserialize_json(
                data["findingDetails"]
            )
        )
    else:
        raise DeserializationError("GetFindingV2Response.finding_details required")
    if "findingType" in data:
        out["finding_type"] = data["findingType"]
    return out
