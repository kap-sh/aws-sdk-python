"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.arn
    import aws_sdk_codeartifact.types.package_group_pattern


class PackageGroupReference(TypedDict):
    arn: NotRequired["aws_sdk_codeartifact.types.arn.Arn"]
    """<p> The ARN of the package group. </p>"""
    pattern: NotRequired[
        "aws_sdk_codeartifact.types.package_group_pattern.PackageGroupPattern"
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
