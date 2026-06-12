"""Generated from Smithy shape ``com.amazonaws.iot#SigningProfileParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_arn
    import aws_sdk_iot.types.certificate_path_on_device
    import aws_sdk_iot.types.platform


class SigningProfileParameter(TypedDict):
    certificate_arn: NotRequired["aws_sdk_iot.types.certificate_arn.CertificateArn"]
    """<p>Certificate ARN.</p>"""
    platform: NotRequired["aws_sdk_iot.types.platform.Platform"]
    """<p>The hardware platform of your device.</p>"""
    certificate_path_on_device: NotRequired[
        "aws_sdk_iot.types.certificate_path_on_device.CertificatePathOnDevice"
    ]
    """<p>The location of the code-signing certificate on your device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfileParameter) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "certificate_path_on_device" in value:
        out["certificatePathOnDevice"] = value["certificate_path_on_device"]
    return out


def deserialize_json(data: dict) -> SigningProfileParameter:
    out: SigningProfileParameter = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "platform" in data:
        out["platform"] = data["platform"]
    if "certificatePathOnDevice" in data:
        out["certificate_path_on_device"] = data["certificatePathOnDevice"]
    return out
