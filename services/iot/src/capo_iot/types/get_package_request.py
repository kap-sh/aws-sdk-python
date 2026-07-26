"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.package_name


class GetPackageRequest(TypedDict, closed=True):
    package_name: "capo_iot.types.package_name.PackageName"
    """<p>The name of the target software package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPackageRequest:
    out: GetPackageRequest = {}  # type: ignore[typeddict-item]
    return out
