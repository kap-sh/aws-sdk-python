"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#GetApplicationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class GetApplicationPolicyRequest(TypedDict, closed=True):
    application_id: "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationPolicyRequest:
    out: GetApplicationPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
