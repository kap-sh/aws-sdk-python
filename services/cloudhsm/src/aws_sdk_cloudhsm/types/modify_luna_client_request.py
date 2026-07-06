"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ModifyLunaClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.certificate
    import aws_sdk_cloudhsm.types.client_arn


class ModifyLunaClientRequest(TypedDict, closed=True):
    client_arn: "aws_sdk_cloudhsm.types.client_arn.ClientArn"
    """<p>The ARN of the client.</p>"""
    certificate: "aws_sdk_cloudhsm.types.certificate.Certificate"
    """<p>The new certificate for the client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyLunaClientRequest) -> dict:
    out: dict = {}
    out["ClientArn"] = value["client_arn"]
    out["Certificate"] = value["certificate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyLunaClientRequest:
    out: ModifyLunaClientRequest = {}  # type: ignore[typeddict-item]
    if "ClientArn" in data:
        out["client_arn"] = data["ClientArn"]
    else:
        raise DeserializationError("ModifyLunaClientRequest.client_arn required")
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    else:
        raise DeserializationError("ModifyLunaClientRequest.certificate required")
    return out
