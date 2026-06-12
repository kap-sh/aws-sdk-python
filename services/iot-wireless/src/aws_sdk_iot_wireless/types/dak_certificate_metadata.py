"""Generated from Smithy shape ``com.amazonaws.iotwireless#DakCertificateMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.ap_id
    import aws_sdk_iot_wireless.types.dak_certificate_id
    import aws_sdk_iot_wireless.types.device_type_id
    import aws_sdk_iot_wireless.types.factory_support
    import aws_sdk_iot_wireless.types.max_allowed_signature


class DakCertificateMetadata(TypedDict):
    certificate_id: "aws_sdk_iot_wireless.types.dak_certificate_id.DakCertificateId"
    """<p>The certificate ID for the DAK.</p>"""
    max_allowed_signature: NotRequired[
        "aws_sdk_iot_wireless.types.max_allowed_signature.MaxAllowedSignature"
    ]
    """<p>The maximum number of signatures that the DAK can sign. A value of <code>-1</code> indicates that there's no device limit.</p>"""
    factory_support: NotRequired[
        "aws_sdk_iot_wireless.types.factory_support.FactorySupport"
    ]
    """<p>Whether factory support has been enabled.</p>"""
    ap_id: NotRequired["aws_sdk_iot_wireless.types.ap_id.ApId"]
    """<p>The advertised product ID (APID) that's used for pre-production and production applications.</p>"""
    device_type_id: NotRequired[
        "aws_sdk_iot_wireless.types.device_type_id.DeviceTypeId"
    ]
    """<p>The device type ID that's used for prototyping applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DakCertificateMetadata) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    if "max_allowed_signature" in value:
        out["MaxAllowedSignature"] = value["max_allowed_signature"]
    if "factory_support" in value:
        out["FactorySupport"] = value["factory_support"]
    if "ap_id" in value:
        out["ApId"] = value["ap_id"]
    if "device_type_id" in value:
        out["DeviceTypeId"] = value["device_type_id"]
    return out


def deserialize_json(data: dict) -> DakCertificateMetadata:
    out: DakCertificateMetadata = {}  # type: ignore[typeddict-item]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    else:
        raise DeserializationError("DakCertificateMetadata.certificate_id required")
    if "MaxAllowedSignature" in data:
        out["max_allowed_signature"] = data["MaxAllowedSignature"]
    if "FactorySupport" in data:
        out["factory_support"] = data["FactorySupport"]
    if "ApId" in data:
        out["ap_id"] = data["ApId"]
    if "DeviceTypeId" in data:
        out["device_type_id"] = data["DeviceTypeId"]
    return out
