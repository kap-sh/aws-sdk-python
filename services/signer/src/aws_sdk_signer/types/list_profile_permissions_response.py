"""Generated from Smithy shape ``com.amazonaws.signer#ListProfilePermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.permissions
    import aws_sdk_signer.types.policy_size_bytes
    import aws_sdk_signer.types.string


class ListProfilePermissionsResponse(TypedDict):
    revision_id: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The identifier for the current revision of profile permissions.</p>"""
    policy_size_bytes: "aws_sdk_signer.types.policy_size_bytes.PolicySizeBytes"
    """<p>Total size of the policy associated with the Signing Profile in bytes.</p>"""
    permissions: NotRequired["aws_sdk_signer.types.permissions.Permissions"]
    """<p>List of permissions associated with the Signing Profile.</p>"""
    next_token: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>String for specifying the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilePermissionsResponse) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    out["policySizeBytes"] = value.get("policy_size_bytes", 0)
    if "permissions" in value:
        import aws_sdk_signer.types.permissions

        out["permissions"] = aws_sdk_signer.types.permissions.serialize_json(
            value["permissions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfilePermissionsResponse:
    out: ListProfilePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "policySizeBytes" in data:
        out["policy_size_bytes"] = data["policySizeBytes"]
    else:
        out["policy_size_bytes"] = 0
    if "permissions" in data:
        import aws_sdk_signer.types.permissions

        out["permissions"] = aws_sdk_signer.types.permissions.deserialize_json(
            data["permissions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
