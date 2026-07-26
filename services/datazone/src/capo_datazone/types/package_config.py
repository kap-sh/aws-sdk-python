"""Generated from Smithy shape ``com.amazonaws.datazone#PackageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.package_manager


class PackageConfig(TypedDict, closed=True):
    package_manager: "capo_datazone.types.package_manager.PackageManager"
    """<p>The package manager for the notebook run environment. The default value is <code>UV</code>.</p>"""
    package_specification: NotRequired["str"]
    """<p>The package specification content for the notebook run environment. The maximum length is 10240 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageConfig) -> dict:
    out: dict = {}
    import capo_datazone.types.package_manager

    out["packageManager"] = capo_datazone.types.package_manager.serialize_json(
        value.get("package_manager", "UV")
    )
    if "package_specification" in value:
        out["packageSpecification"] = value["package_specification"]
    return out


def deserialize_json(data: dict) -> PackageConfig:
    out: PackageConfig = {}  # type: ignore[typeddict-item]
    if "packageManager" in data:
        import capo_datazone.types.package_manager

        out["package_manager"] = capo_datazone.types.package_manager.deserialize_json(
            data["packageManager"]
        )
    else:
        out["package_manager"] = "UV"
    if "packageSpecification" in data:
        out["package_specification"] = data["packageSpecification"]
    return out
