"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DescribeHsmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hsm_arn
    import aws_sdk_cloudhsm.types.hsm_serial_number


class DescribeHsmRequest(TypedDict, closed=True):
    hsm_arn: NotRequired["aws_sdk_cloudhsm.types.hsm_arn.HsmArn"]
    """<p>The ARN of the HSM. Either the <code>HsmArn</code> or the <code>SerialNumber</code> parameter must be specified.</p>"""
    hsm_serial_number: NotRequired[
        "aws_sdk_cloudhsm.types.hsm_serial_number.HsmSerialNumber"
    ]
    """<p>The serial number of the HSM. Either the <code>HsmArn</code> or the <code>HsmSerialNumber</code> parameter must be specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHsmRequest) -> dict:
    out: dict = {}
    if "hsm_arn" in value:
        out["HsmArn"] = value["hsm_arn"]
    if "hsm_serial_number" in value:
        out["HsmSerialNumber"] = value["hsm_serial_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHsmRequest:
    out: DescribeHsmRequest = {}  # type: ignore[typeddict-item]
    if "HsmArn" in data:
        out["hsm_arn"] = data["HsmArn"]
    if "HsmSerialNumber" in data:
        out["hsm_serial_number"] = data["HsmSerialNumber"]
    return out
