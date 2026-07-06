"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.identity
    import aws_sdk_iotsitewise.types.permission
    import aws_sdk_iotsitewise.types.resource
    import aws_sdk_iotsitewise.types.tag_map


class CreateAccessPolicyRequest(TypedDict, closed=True):
    access_policy_identity: "aws_sdk_iotsitewise.types.identity.Identity"
    """<p>The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.</p>"""
    access_policy_resource: "aws_sdk_iotsitewise.types.resource.Resource"
    """<p>The IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.</p>"""
    access_policy_permission: "aws_sdk_iotsitewise.types.permission.Permission"
    """<p>The permission level for this access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    tags: NotRequired["aws_sdk_iotsitewise.types.tag_map.TagMap"]
    r"""<p>A list of key-value pairs that contain metadata for the access policy. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessPolicyRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.identity

    out["accessPolicyIdentity"] = aws_sdk_iotsitewise.types.identity.serialize_json(
        value["access_policy_identity"]
    )
    import aws_sdk_iotsitewise.types.resource

    out["accessPolicyResource"] = aws_sdk_iotsitewise.types.resource.serialize_json(
        value["access_policy_resource"]
    )
    import aws_sdk_iotsitewise.types.permission

    out["accessPolicyPermission"] = aws_sdk_iotsitewise.types.permission.serialize_json(
        value["access_policy_permission"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAccessPolicyRequest:
    out: CreateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if "accessPolicyIdentity" in data:
        import aws_sdk_iotsitewise.types.identity

        out["access_policy_identity"] = (
            aws_sdk_iotsitewise.types.identity.deserialize_json(
                data["accessPolicyIdentity"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccessPolicyRequest.access_policy_identity required"
        )
    if "accessPolicyResource" in data:
        import aws_sdk_iotsitewise.types.resource

        out["access_policy_resource"] = (
            aws_sdk_iotsitewise.types.resource.deserialize_json(
                data["accessPolicyResource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccessPolicyRequest.access_policy_resource required"
        )
    if "accessPolicyPermission" in data:
        import aws_sdk_iotsitewise.types.permission

        out["access_policy_permission"] = (
            aws_sdk_iotsitewise.types.permission.deserialize_json(
                data["accessPolicyPermission"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccessPolicyRequest.access_policy_permission required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out
