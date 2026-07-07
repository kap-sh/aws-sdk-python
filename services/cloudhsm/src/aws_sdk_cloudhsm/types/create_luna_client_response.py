"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateLunaClientResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.client_arn


class CreateLunaClientResponse(TypedDict, closed=True):
    client_arn: NotRequired["aws_sdk_cloudhsm.types.client_arn.ClientArn"]
    """<p>The ARN of the client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLunaClientResponse) -> dict:
    out: dict = {}
    if "client_arn" in value:
        out["ClientArn"] = value["client_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLunaClientResponse:
    out: CreateLunaClientResponse = {}  # type: ignore[typeddict-item]
    if "ClientArn" in data:
        out["client_arn"] = data["ClientArn"]
    return out
