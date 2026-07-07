"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeFleetRoleForReadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aws_credentials


class AssumeFleetRoleForReadResponse(TypedDict, closed=True):
    credentials: "aws_sdk_deadline.types.aws_credentials.AwsCredentials"
    """<p>The credentials for the fleet role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeFleetRoleForReadResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.aws_credentials

    out["credentials"] = aws_sdk_deadline.types.aws_credentials.serialize_json(
        value["credentials"]
    )
    return out


def deserialize_json(data: dict) -> AssumeFleetRoleForReadResponse:
    out: AssumeFleetRoleForReadResponse = {}  # type: ignore[typeddict-item]
    if "credentials" in data:
        import aws_sdk_deadline.types.aws_credentials

        out["credentials"] = aws_sdk_deadline.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    else:
        raise DeserializationError(
            "AssumeFleetRoleForReadResponse.credentials required"
        )
    return out
