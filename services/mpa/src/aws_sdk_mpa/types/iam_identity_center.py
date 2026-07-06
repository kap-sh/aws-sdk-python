"""Generated from Smithy shape ``com.amazonaws.mpa#IamIdentityCenter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.idc_instance_arn
    import aws_sdk_mpa.types.string


class IamIdentityCenter(TypedDict, closed=True):
    instance_arn: "aws_sdk_mpa.types.idc_instance_arn.IdcInstanceArn"
    """<p>Amazon Resource Name (ARN) for the IAM Identity Center instance.</p>"""
    region: "aws_sdk_mpa.types.string.String"
    """<p>Amazon Web Services Region where the IAM Identity Center instance is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamIdentityCenter) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> IamIdentityCenter:
    out: IamIdentityCenter = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("IamIdentityCenter.instance_arn required")
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("IamIdentityCenter.region required")
    return out
