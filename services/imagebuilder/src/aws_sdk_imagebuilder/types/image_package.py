"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImagePackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string


class ImagePackage(TypedDict, closed=True):
    package_name: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the package that's reported to the operating system package manager.</p>"""
    package_version: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the package that's reported to the operating system package manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImagePackage) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "package_version" in value:
        out["packageVersion"] = value["package_version"]
    return out


def deserialize_json(data: dict) -> ImagePackage:
    out: ImagePackage = {}  # type: ignore[typeddict-item]
    if "packageName" in data:
        out["package_name"] = data["packageName"]
    if "packageVersion" in data:
        out["package_version"] = data["packageVersion"]
    return out
