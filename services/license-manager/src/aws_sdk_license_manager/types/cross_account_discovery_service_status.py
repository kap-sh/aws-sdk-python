"""Generated from Smithy shape ``com.amazonaws.licensemanager#CrossAccountDiscoveryServiceStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class CrossAccountDiscoveryServiceStatus(TypedDict):
    message: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Status message for cross-account discovery service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountDiscoveryServiceStatus) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrossAccountDiscoveryServiceStatus:
    out: CrossAccountDiscoveryServiceStatus = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
