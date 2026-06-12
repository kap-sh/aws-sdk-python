"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeFleetRoleForWorkerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aws_credentials


class AssumeFleetRoleForWorkerResponse(TypedDict):
    credentials: "aws_sdk_deadline.types.aws_credentials.AwsCredentials"
    """<p>The credentials for the worker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeFleetRoleForWorkerResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.aws_credentials

    out["credentials"] = aws_sdk_deadline.types.aws_credentials.serialize_json(
        value["credentials"]
    )
    return out


def deserialize_json(data: dict) -> AssumeFleetRoleForWorkerResponse:
    out: AssumeFleetRoleForWorkerResponse = {}  # type: ignore[typeddict-item]
    if "credentials" in data:
        import aws_sdk_deadline.types.aws_credentials

        out["credentials"] = aws_sdk_deadline.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    else:
        raise DeserializationError(
            "AssumeFleetRoleForWorkerResponse.credentials required"
        )
    return out
