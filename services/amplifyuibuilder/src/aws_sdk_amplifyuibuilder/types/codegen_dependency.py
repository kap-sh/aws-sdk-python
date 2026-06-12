"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenDependency``."""

from typing import TypedDict
from typing_extensions import NotRequired

class CodegenDependency(TypedDict):
    name: NotRequired["str"]
    """<p>Name of the dependency package.</p>"""
    supported_version: NotRequired["str"]
    """<p>Indicates the version of the supported dependency package.</p>"""
    is_sem_ver: NotRequired["bool"]
    """<p>Determines if the dependency package is using Semantic versioning. If set to true, it indicates that the dependency package uses Semantic versioning.</p>"""
    reason: NotRequired["str"]
    """<p>Indicates the reason to include the dependency package in your project code.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CodegenDependency) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "supported_version" in value:
        out["supportedVersion"] = value["supported_version"]
    if "is_sem_ver" in value:
        out["isSemVer"] = value["is_sem_ver"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CodegenDependency:
    out: CodegenDependency = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "supportedVersion" in data:
        out["supported_version"] = data["supportedVersion"]
    if "isSemVer" in data:
        out["is_sem_ver"] = data["isSemVer"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out