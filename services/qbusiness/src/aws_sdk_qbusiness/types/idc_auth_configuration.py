"""Generated from Smithy shape ``com.amazonaws.qbusiness#IdcAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.idc_application_arn
    import aws_sdk_qbusiness.types.role_arn


class IdcAuthConfiguration(TypedDict, closed=True):
    idc_application_arn: "aws_sdk_qbusiness.types.idc_application_arn.IdcApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center Application used to configure authentication.</p>"""
    role_arn: "aws_sdk_qbusiness.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role with permissions to perform actions on Amazon Web Services services on your behalf.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdcAuthConfiguration) -> dict:
    out: dict = {}
    out["idcApplicationArn"] = value["idc_application_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IdcAuthConfiguration:
    out: IdcAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "idcApplicationArn" in data:
        out["idc_application_arn"] = data["idcApplicationArn"]
    else:
        raise DeserializationError("IdcAuthConfiguration.idc_application_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("IdcAuthConfiguration.role_arn required")
    return out
