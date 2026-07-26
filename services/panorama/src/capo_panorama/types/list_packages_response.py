"""Generated from Smithy shape ``com.amazonaws.panorama#ListPackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.next_token
    import capo_panorama.types.package_list


class ListPackagesResponse(TypedDict, closed=True):
    packages: NotRequired["capo_panorama.types.package_list.PackageList"]
    """<p>A list of packages.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesResponse) -> dict:
    out: dict = {}
    if "packages" in value:
        import capo_panorama.types.package_list

        out["Packages"] = capo_panorama.types.package_list.serialize_json(
            value["packages"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackagesResponse:
    out: ListPackagesResponse = {}  # type: ignore[typeddict-item]
    if "Packages" in data:
        import capo_panorama.types.package_list

        out["packages"] = capo_panorama.types.package_list.deserialize_json(
            data["Packages"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
