"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateAccessTokenOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.access_token_value
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short
    import aws_sdk_route53globalresolver.types.token_status


class CreateAccessTokenOutput(TypedDict):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier for the access token.</p>"""
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access token.</p>"""
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the access token was created.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view associated with this access token.</p>"""
    expires_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the access token expires.</p>"""
    name: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the access token.</p>"""
    status: "aws_sdk_route53globalresolver.types.token_status.TokenStatus"
    """<p>The operational status of the access token.</p>"""
    value: "aws_sdk_route53globalresolver.types.access_token_value.AccessTokenValue"
    """<p>The access token value. This token should be included in DoH and DoT requests for authentication. Keep this value secure as it provides access to your Route 53 Global Resolver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessTokenOutput) -> dict:
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
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_route53globalresolver.types.token_status

    out["status"] = aws_sdk_route53globalresolver.types.token_status.serialize_json(
        value["status"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CreateAccessTokenOutput:
    out: CreateAccessTokenOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateAccessTokenOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateAccessTokenOutput.arn required")
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
        raise DeserializationError("CreateAccessTokenOutput.created_at required")
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("CreateAccessTokenOutput.dns_view_id required")
    if "expiresAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["expires_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["expiresAt"]
            )
        )
    else:
        raise DeserializationError("CreateAccessTokenOutput.expires_at required")
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
        raise DeserializationError("CreateAccessTokenOutput.status required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("CreateAccessTokenOutput.value required")
    return out
