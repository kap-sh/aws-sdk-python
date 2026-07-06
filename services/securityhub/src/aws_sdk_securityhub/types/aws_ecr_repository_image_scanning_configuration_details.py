"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcrRepositoryImageScanningConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsEcrRepositoryImageScanningConfigurationDetails(TypedDict, closed=True):
    scan_on_push: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to scan images after they are pushed to a repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrRepositoryImageScanningConfigurationDetails) -> dict:
    out: dict = {}
    if "scan_on_push" in value:
        out["ScanOnPush"] = value["scan_on_push"]
    return out


def deserialize_json(data: dict) -> AwsEcrRepositoryImageScanningConfigurationDetails:
    out: AwsEcrRepositoryImageScanningConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "ScanOnPush" in data:
        out["scan_on_push"] = data["ScanOnPush"]
    return out
