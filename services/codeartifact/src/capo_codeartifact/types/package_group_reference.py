"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.package_group_pattern


class PackageGroupReference(TypedDict, closed=True):
    arn: NotRequired["capo_codeartifact.types.arn.Arn"]
    """<p> The ARN of the package group. </p>"""
    pattern: NotRequired[
        "capo_codeartifact.types.package_group_pattern.PackageGroupPattern"
    ]
    """<p> The pattern of the package group. The pattern determines which packages are associated with the package group, and is also the identifier of the package group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupReference) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "pattern" in value:
        out["pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> PackageGroupReference:
    out: PackageGroupReference = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "pattern" in data:
        out["pattern"] = data["pattern"]
    return out
