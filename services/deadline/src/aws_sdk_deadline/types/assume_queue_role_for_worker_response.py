"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForWorkerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aws_credentials


class AssumeQueueRoleForWorkerResponse(TypedDict):
    credentials: NotRequired["aws_sdk_deadline.types.aws_credentials.AwsCredentials"]
    """<p>The Amazon Web Services credentials for the role that the worker is assuming.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForWorkerResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import aws_sdk_deadline.types.aws_credentials

        out["credentials"] = aws_sdk_deadline.types.aws_credentials.serialize_json(
            value["credentials"]
        )
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForWorkerResponse:
    out: AssumeQueueRoleForWorkerResponse = {}  # type: ignore[typeddict-item]
    if "credentials" in data:
        import aws_sdk_deadline.types.aws_credentials

        out["credentials"] = aws_sdk_deadline.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    return out
