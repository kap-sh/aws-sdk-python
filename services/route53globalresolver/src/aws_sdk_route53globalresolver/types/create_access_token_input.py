"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateAccessTokenInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short
    import aws_sdk_route53globalresolver.types.tags


class CreateAccessTokenInput(TypedDict):
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view to associate with this token.</p>"""
    expires_at: NotRequired[
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    ]
    """<p>The date and time when the token expires. Tokens can have a minimum expiration of 30 days and maximum of 365 days from creation.</p>"""
    name: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>A descriptive name for the access token.</p>"""
    tags: NotRequired["aws_sdk_route53globalresolver.types.tags.Tags"]
    """<p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessTokenInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "expires_at" in value:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["expiresAt"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
                value["expires_at"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateAccessTokenInput:
    out: CreateAccessTokenInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "expiresAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["expires_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["expiresAt"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
