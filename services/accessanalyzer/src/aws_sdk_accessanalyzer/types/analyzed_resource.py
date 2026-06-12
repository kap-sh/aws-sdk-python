"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzedResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.action_list
    import aws_sdk_accessanalyzer.types.finding_status
    import aws_sdk_accessanalyzer.types.resource_arn
    import aws_sdk_accessanalyzer.types.resource_type
    import aws_sdk_accessanalyzer.types.shared_via_list
    import aws_sdk_accessanalyzer.types.timestamp


class AnalyzedResource(TypedDict):
    resource_arn: "aws_sdk_accessanalyzer.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource that was analyzed.</p>"""
    resource_type: "aws_sdk_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of the resource that was analyzed.</p>"""
    created_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was created.</p>"""
    analyzed_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the resource was analyzed.</p>"""
    updated_at: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the finding was updated.</p>"""
    is_public: "bool"
    """<p>Indicates whether the policy that generated the finding grants public access to the resource.</p>"""
    actions: NotRequired["aws_sdk_accessanalyzer.types.action_list.ActionList"]
    """<p>The actions that an external principal is granted permission to use by the policy that generated the finding.</p>"""
    shared_via: NotRequired[
        "aws_sdk_accessanalyzer.types.shared_via_list.SharedViaList"
    ]
    """<p>Indicates how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.</p>"""
    status: NotRequired["aws_sdk_accessanalyzer.types.finding_status.FindingStatus"]
    """<p>The current status of the finding generated from the analyzed resource.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    error: NotRequired["str"]
    """<p>An error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzedResource) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["resourceType"] = value["resource_type"]
    import aws_sdk_accessanalyzer.types.timestamp

    out["createdAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["analyzedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["analyzed_at"]
    )
    import aws_sdk_accessanalyzer.types.timestamp

    out["updatedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    out["isPublic"] = value["is_public"]
    if "actions" in value:
        import aws_sdk_accessanalyzer.types.action_list

        out["actions"] = aws_sdk_accessanalyzer.types.action_list.serialize_json(
            value["actions"]
        )
    if "shared_via" in value:
        import aws_sdk_accessanalyzer.types.shared_via_list

        out["sharedVia"] = aws_sdk_accessanalyzer.types.shared_via_list.serialize_json(
            value["shared_via"]
        )
    if "status" in value:
        out["status"] = value["status"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> AnalyzedResource:
    out: AnalyzedResource = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("AnalyzedResource.resource_arn required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("AnalyzedResource.resource_type required")
    if "createdAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["created_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AnalyzedResource.created_at required")
    if "analyzedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["analyzed_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["analyzedAt"]
        )
    else:
        raise DeserializationError("AnalyzedResource.analyzed_at required")
    if "updatedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["updated_at"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AnalyzedResource.updated_at required")
    if "isPublic" in data:
        out["is_public"] = data["isPublic"]
    else:
        raise DeserializationError("AnalyzedResource.is_public required")
    if "actions" in data:
        import aws_sdk_accessanalyzer.types.action_list

        out["actions"] = aws_sdk_accessanalyzer.types.action_list.deserialize_json(
            data["actions"]
        )
    if "sharedVia" in data:
        import aws_sdk_accessanalyzer.types.shared_via_list

        out["shared_via"] = (
            aws_sdk_accessanalyzer.types.shared_via_list.deserialize_json(
                data["sharedVia"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "resourceOwnerAccount" in data:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        raise DeserializationError("AnalyzedResource.resource_owner_account required")
    if "error" in data:
        out["error"] = data["error"]
    return out
