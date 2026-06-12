"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientCertAuthSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.ocsp_url


class ClientCertAuthSettings(TypedDict):
    ocsp_url: NotRequired["aws_sdk_directory_service.types.ocsp_url.OCSPUrl"]
    """<p>Specifies the URL of the default OCSP server used to check for revocation status. A secondary value to any OCSP address found in the AIA extension of the user certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientCertAuthSettings) -> dict:
    out: dict = {}
    if "ocsp_url" in value:
        out["OCSPUrl"] = value["ocsp_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientCertAuthSettings:
    out: ClientCertAuthSettings = {}  # type: ignore[typeddict-item]
    if "OCSPUrl" in data:
        out["ocsp_url"] = data["OCSPUrl"]
    return out
