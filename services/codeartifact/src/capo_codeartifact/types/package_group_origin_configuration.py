"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupOriginConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_origin_restrictions


class PackageGroupOriginConfiguration(TypedDict, closed=True):
    restrictions: NotRequired[
        "capo_codeartifact.types.package_group_origin_restrictions.PackageGroupOriginRestrictions"
    ]
    """<p>The origin configuration settings that determine how package versions can enter repositories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupOriginConfiguration) -> dict:
    out: dict = {}
    if "restrictions" in value:
        import capo_codeartifact.types.package_group_origin_restrictions

        out["restrictions"] = (
            capo_codeartifact.types.package_group_origin_restrictions.serialize_json(
                value["restrictions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageGroupOriginConfiguration:
    out: PackageGroupOriginConfiguration = {}  # type: ignore[typeddict-item]
    if "restrictions" in data:
        import capo_codeartifact.types.package_group_origin_restrictions

        out["restrictions"] = (
            capo_codeartifact.types.package_group_origin_restrictions.deserialize_json(
                data["restrictions"]
            )
        )
    return out
