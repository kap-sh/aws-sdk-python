"""Generated from Smithy shape ``com.amazonaws.ssm#StartAccessRequestResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.access_request_id


class StartAccessRequestResponse(TypedDict):
    access_request_id: NotRequired[
        "aws_sdk_ssm.types.access_request_id.AccessRequestId"
    ]
    """<p>The ID of the access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAccessRequestResponse) -> dict:
    out: dict = {}
    if "access_request_id" in value:
        out["AccessRequestId"] = value["access_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAccessRequestResponse:
    out: StartAccessRequestResponse = {}  # type: ignore[typeddict-item]
    if "AccessRequestId" in data:
        out["access_request_id"] = data["AccessRequestId"]
    return out
