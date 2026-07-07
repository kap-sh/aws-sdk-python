"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteAccessTokenOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.token_status


class DeleteAccessTokenOutput(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted access token.</p>"""
    status: "aws_sdk_route53globalresolver.types.token_status.TokenStatus"
    """<p>The final status of the deleted access token.</p>"""
    deleted_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the access token was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessTokenOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_route53globalresolver.types.token_status

    out["status"] = aws_sdk_route53globalresolver.types.token_status.serialize_json(
        value["status"]
    )
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["deletedAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["deleted_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAccessTokenOutput:
    out: DeleteAccessTokenOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteAccessTokenOutput.id required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.token_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.token_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteAccessTokenOutput.status required")
    if "deletedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["deleted_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["deletedAt"]
            )
        )
    else:
        raise DeserializationError("DeleteAccessTokenOutput.deleted_at required")
    return out
