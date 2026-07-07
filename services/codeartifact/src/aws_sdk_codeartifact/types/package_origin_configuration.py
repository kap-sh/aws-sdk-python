"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageOriginConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_origin_restrictions


class PackageOriginConfiguration(TypedDict, closed=True):
    restrictions: NotRequired[
        "aws_sdk_codeartifact.types.package_origin_restrictions.PackageOriginRestrictions"
    ]
    """<p>A <code>PackageOriginRestrictions</code> object that contains information about the upstream and publish package origin configuration for the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageOriginConfiguration) -> dict:
    out: dict = {}
    if "restrictions" in value:
        import aws_sdk_codeartifact.types.package_origin_restrictions

        out["restrictions"] = (
            aws_sdk_codeartifact.types.package_origin_restrictions.serialize_json(
                value["restrictions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageOriginConfiguration:
    out: PackageOriginConfiguration = {}  # type: ignore[typeddict-item]
    if "restrictions" in data:
        import aws_sdk_codeartifact.types.package_origin_restrictions

        out["restrictions"] = (
            aws_sdk_codeartifact.types.package_origin_restrictions.deserialize_json(
                data["restrictions"]
            )
        )
    return out
