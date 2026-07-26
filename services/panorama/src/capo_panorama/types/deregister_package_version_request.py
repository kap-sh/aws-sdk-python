"""Generated from Smithy shape ``com.amazonaws.panorama#DeregisterPackageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.node_package_id
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version
    import capo_panorama.types.package_owner_account


class DeregisterPackageVersionRequest(TypedDict, closed=True):
    owner_account: NotRequired[
        "capo_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>An owner account.</p>"""
    package_id: "capo_panorama.types.node_package_id.NodePackageId"
    """<p>A package ID.</p>"""
    package_version: "capo_panorama.types.node_package_version.NodePackageVersion"
    """<p>A package version.</p>"""
    patch_version: (
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>A patch version.</p>"""
    updated_latest_patch_version: NotRequired[
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    ]
    """<p>If the version was marked latest, the new version to maker as latest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterPackageVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterPackageVersionRequest:
    out: DeregisterPackageVersionRequest = {}  # type: ignore[typeddict-item]
    return out
