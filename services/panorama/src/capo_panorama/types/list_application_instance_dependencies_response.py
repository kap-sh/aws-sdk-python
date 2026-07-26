"""Generated from Smithy shape ``com.amazonaws.panorama#ListApplicationInstanceDependenciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.next_token
    import capo_panorama.types.package_objects


class ListApplicationInstanceDependenciesResponse(TypedDict, closed=True):
    package_objects: NotRequired["capo_panorama.types.package_objects.PackageObjects"]
    """<p>A list of package objects.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationInstanceDependenciesResponse) -> dict:
    out: dict = {}
    if "package_objects" in value:
        import capo_panorama.types.package_objects

        out["PackageObjects"] = capo_panorama.types.package_objects.serialize_json(
            value["package_objects"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationInstanceDependenciesResponse:
    out: ListApplicationInstanceDependenciesResponse = {}  # type: ignore[typeddict-item]
    if "PackageObjects" in data:
        import capo_panorama.types.package_objects

        out["package_objects"] = capo_panorama.types.package_objects.deserialize_json(
            data["PackageObjects"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
