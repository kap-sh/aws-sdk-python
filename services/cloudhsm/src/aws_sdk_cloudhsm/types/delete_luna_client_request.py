"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DeleteLunaClientRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.client_arn


class DeleteLunaClientRequest(TypedDict):
    client_arn: "aws_sdk_cloudhsm.types.client_arn.ClientArn"
    """<p>The ARN of the client to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLunaClientRequest) -> dict:
    out: dict = {}
    out["ClientArn"] = value["client_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLunaClientRequest:
    out: DeleteLunaClientRequest = {}  # type: ignore[typeddict-item]
    if "ClientArn" in data:
        out["client_arn"] = data["ClientArn"]
    else:
        raise DeserializationError("DeleteLunaClientRequest.client_arn required")
    return out
