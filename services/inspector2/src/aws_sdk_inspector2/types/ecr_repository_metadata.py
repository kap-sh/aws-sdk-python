"""Generated from Smithy shape ``com.amazonaws.inspector2#EcrRepositoryMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ecr_scan_frequency


class EcrRepositoryMetadata(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the Amazon ECR repository.</p>"""
    scan_frequency: NotRequired[
        "aws_sdk_inspector2.types.ecr_scan_frequency.EcrScanFrequency"
    ]
    """<p>The frequency of scans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrRepositoryMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "scan_frequency" in value:
        out["scanFrequency"] = value["scan_frequency"]
    return out


def deserialize_json(data: dict) -> EcrRepositoryMetadata:
    out: EcrRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "scanFrequency" in data:
        out["scan_frequency"] = data["scanFrequency"]
    return out
