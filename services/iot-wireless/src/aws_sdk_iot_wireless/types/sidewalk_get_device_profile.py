"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkGetDeviceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.application_server_public_key
    import aws_sdk_iot_wireless.types.dak_certificate_metadata_list
    import aws_sdk_iot_wireless.types.qualification_status


class SidewalkGetDeviceProfile(TypedDict):
    application_server_public_key: NotRequired[
        "aws_sdk_iot_wireless.types.application_server_public_key.ApplicationServerPublicKey"
    ]
    """<p>The Sidewalk application server public key.</p>"""
    qualification_status: NotRequired[
        "aws_sdk_iot_wireless.types.qualification_status.QualificationStatus"
    ]
    """<p>Gets information about the certification status of a Sidewalk device profile.</p>"""
    dak_certificate_metadata: NotRequired[
        "aws_sdk_iot_wireless.types.dak_certificate_metadata_list.DakCertificateMetadataList"
    ]
    """<p>The DAK certificate information of the Sidewalk device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkGetDeviceProfile) -> dict:
    out: dict = {}
    if "application_server_public_key" in value:
        out["ApplicationServerPublicKey"] = value["application_server_public_key"]
    if "qualification_status" in value:
        out["QualificationStatus"] = value["qualification_status"]
    if "dak_certificate_metadata" in value:
        import aws_sdk_iot_wireless.types.dak_certificate_metadata_list

        out["DakCertificateMetadata"] = (
            aws_sdk_iot_wireless.types.dak_certificate_metadata_list.serialize_json(
                value["dak_certificate_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkGetDeviceProfile:
    out: SidewalkGetDeviceProfile = {}  # type: ignore[typeddict-item]
    if "ApplicationServerPublicKey" in data:
        out["application_server_public_key"] = data["ApplicationServerPublicKey"]
    if "QualificationStatus" in data:
        out["qualification_status"] = data["QualificationStatus"]
    if "DakCertificateMetadata" in data:
        import aws_sdk_iot_wireless.types.dak_certificate_metadata_list

        out["dak_certificate_metadata"] = (
            aws_sdk_iot_wireless.types.dak_certificate_metadata_list.deserialize_json(
                data["DakCertificateMetadata"]
            )
        )
    return out
