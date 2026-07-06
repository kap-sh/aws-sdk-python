"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AccessPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.identity
    import aws_sdk_iotsitewise.types.permission
    import aws_sdk_iotsitewise.types.resource
    import aws_sdk_iotsitewise.types.timestamp


class AccessPolicySummary(TypedDict, closed=True):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the access policy.</p>"""
    identity: "aws_sdk_iotsitewise.types.identity.Identity"
    """<p>The identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user).</p>"""
    resource: "aws_sdk_iotsitewise.types.resource.Resource"
    """<p>The IoT SiteWise Monitor resource (a portal or project).</p>"""
    permission: "aws_sdk_iotsitewise.types.permission.Permission"
    """<p>The permissions for the access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>"""
    creation_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the access policy was created, in Unix epoch time.</p>"""
    last_update_date: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the access policy was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPolicySummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_iotsitewise.types.identity

    out["identity"] = aws_sdk_iotsitewise.types.identity.serialize_json(
        value["identity"]
    )
    import aws_sdk_iotsitewise.types.resource

    out["resource"] = aws_sdk_iotsitewise.types.resource.serialize_json(
        value["resource"]
    )
    import aws_sdk_iotsitewise.types.permission

    out["permission"] = aws_sdk_iotsitewise.types.permission.serialize_json(
        value["permission"]
    )
    if "creation_date" in value:
        import aws_sdk_iotsitewise.types.timestamp

        out["creationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_update_date" in value:
        import aws_sdk_iotsitewise.types.timestamp

        out["lastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["last_update_date"]
        )
    return out


def deserialize_json(data: dict) -> AccessPolicySummary:
    out: AccessPolicySummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AccessPolicySummary.id required")
    if "identity" in data:
        import aws_sdk_iotsitewise.types.identity

        out["identity"] = aws_sdk_iotsitewise.types.identity.deserialize_json(
            data["identity"]
        )
    else:
        raise DeserializationError("AccessPolicySummary.identity required")
    if "resource" in data:
        import aws_sdk_iotsitewise.types.resource

        out["resource"] = aws_sdk_iotsitewise.types.resource.deserialize_json(
            data["resource"]
        )
    else:
        raise DeserializationError("AccessPolicySummary.resource required")
    if "permission" in data:
        import aws_sdk_iotsitewise.types.permission

        out["permission"] = aws_sdk_iotsitewise.types.permission.deserialize_json(
            data["permission"]
        )
    else:
        raise DeserializationError("AccessPolicySummary.permission required")
    if "creationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["creation_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if "lastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["last_update_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    return out
