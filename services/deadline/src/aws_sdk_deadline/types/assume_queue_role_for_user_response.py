"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aws_credentials


class AssumeQueueRoleForUserResponse(TypedDict):
    credentials: "aws_sdk_deadline.types.aws_credentials.AwsCredentials"
    """<p>The credentials for the queue role that a user has access to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForUserResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.aws_credentials

    out["credentials"] = aws_sdk_deadline.types.aws_credentials.serialize_json(
        value["credentials"]
    )
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForUserResponse:
    out: AssumeQueueRoleForUserResponse = {}  # type: ignore[typeddict-item]
    if "credentials" in data:
        import aws_sdk_deadline.types.aws_credentials

        out["credentials"] = aws_sdk_deadline.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    else:
        raise DeserializationError(
            "AssumeQueueRoleForUserResponse.credentials required"
        )
    return out
