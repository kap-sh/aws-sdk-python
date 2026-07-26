"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxVolumesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_volumes
    import capo_finspace.types.pagination_token


class ListKxVolumesResponse(TypedDict, closed=True):
    kx_volume_summaries: NotRequired["capo_finspace.types.kx_volumes.KxVolumes"]
    """<p> A summary of volumes. </p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxVolumesResponse) -> dict:
    out: dict = {}
    if "kx_volume_summaries" in value:
        import capo_finspace.types.kx_volumes

        out["kxVolumeSummaries"] = capo_finspace.types.kx_volumes.serialize_json(
            value["kx_volume_summaries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxVolumesResponse:
    out: ListKxVolumesResponse = {}  # type: ignore[typeddict-item]
    if "kxVolumeSummaries" in data:
        import capo_finspace.types.kx_volumes

        out["kx_volume_summaries"] = capo_finspace.types.kx_volumes.deserialize_json(
            data["kxVolumeSummaries"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
