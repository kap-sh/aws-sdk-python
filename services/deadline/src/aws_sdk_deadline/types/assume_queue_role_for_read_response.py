"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForReadResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aws_credentials


class AssumeQueueRoleForReadResponse(TypedDict):
    credentials: "aws_sdk_deadline.types.aws_credentials.AwsCredentials"
    """<p>The credentials for the queue role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForReadResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.aws_credentials

    out["credentials"] = aws_sdk_deadline.types.aws_credentials.serialize_json(
        value["credentials"]
    )
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForReadResponse:
    out: AssumeQueueRoleForReadResponse = {}  # type: ignore[typeddict-item]
    if "credentials" in data:
        import aws_sdk_deadline.types.aws_credentials

        out["credentials"] = aws_sdk_deadline.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    else:
        raise DeserializationError(
            "AssumeQueueRoleForReadResponse.credentials required"
        )
    return out
