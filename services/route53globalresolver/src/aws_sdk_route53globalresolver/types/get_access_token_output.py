"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetAccessTokenOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.access_token_value
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short
    import aws_sdk_route53globalresolver.types.token_status


class GetAccessTokenOutput(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the token.</p>"""
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the token.</p>"""
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The time and date the token was created.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the DNS view the token is associated to.</p>"""
    expires_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The token's expiration time and date.</p>"""
    global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the Global Resolver.</p>"""
    name: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>Name of the token.</p>"""
    status: "aws_sdk_route53globalresolver.types.token_status.TokenStatus"
    """<p>The operational status of the token.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The time and date the token was created.</p>"""
    value: "aws_sdk_route53globalresolver.types.access_token_value.AccessTokenValue"
    """<p>The value of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessTokenOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    out["dnsViewId"] = value["dns_view_id"]
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["expiresAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["expires_at"]
        )
    )
    out["globalResolverId"] = value["global_resolver_id"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_route53globalresolver.types.token_status

    out["status"] = aws_sdk_route53globalresolver.types.token_status.serialize_json(
        value["status"]
    )
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> GetAccessTokenOutput:
    out: GetAccessTokenOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetAccessTokenOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetAccessTokenOutput.arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetAccessTokenOutput.created_at required")
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("GetAccessTokenOutput.dns_view_id required")
    if "expiresAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["expires_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["expiresAt"]
            )
        )
    else:
        raise DeserializationError("GetAccessTokenOutput.expires_at required")
    if "globalResolverId" in data:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError("GetAccessTokenOutput.global_resolver_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_route53globalresolver.types.token_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.token_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetAccessTokenOutput.status required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetAccessTokenOutput.updated_at required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("GetAccessTokenOutput.value required")
    return out
