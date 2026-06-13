"""Generated from Smithy shape ``com.amazonaws.securityagent#IdCConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.id_c_application_arn
    import aws_sdk_securityagent.types.id_c_instance_arn


class IdCConfiguration(TypedDict):
    idc_application_arn: NotRequired[
        "aws_sdk_securityagent.types.id_c_application_arn.IdCApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application.</p>"""
    idc_instance_arn: NotRequired[
        "aws_sdk_securityagent.types.id_c_instance_arn.IdCInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdCConfiguration) -> dict:
    out: dict = {}
    if "idc_application_arn" in value:
        out["idcApplicationArn"] = value["idc_application_arn"]
    if "idc_instance_arn" in value:
        out["idcInstanceArn"] = value["idc_instance_arn"]
    return out


def deserialize_json(data: dict) -> IdCConfiguration:
    out: IdCConfiguration = {}  # type: ignore[typeddict-item]
    if "idcApplicationArn" in data:
        out["idc_application_arn"] = data["idcApplicationArn"]
    if "idcInstanceArn" in data:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    return out
