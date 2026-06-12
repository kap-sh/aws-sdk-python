"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ModifyLunaClientResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.client_arn


class ModifyLunaClientResponse(TypedDict):
    client_arn: NotRequired["aws_sdk_cloudhsm.types.client_arn.ClientArn"]
    """<p>The ARN of the client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyLunaClientResponse) -> dict:
    out: dict = {}
    if "client_arn" in value:
        out["ClientArn"] = value["client_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyLunaClientResponse:
    out: ModifyLunaClientResponse = {}  # type: ignore[typeddict-item]
    if "ClientArn" in data:
        out["client_arn"] = data["ClientArn"]
    return out
