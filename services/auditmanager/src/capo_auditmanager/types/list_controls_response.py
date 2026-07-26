"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_metadata_list
    import capo_auditmanager.types.token


class ListControlsResponse(TypedDict, closed=True):
    control_metadata_list: NotRequired[
        "capo_auditmanager.types.control_metadata_list.ControlMetadataList"
    ]
    """<p> A list of metadata that the <code>ListControls</code> API returns for each control.</p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlsResponse) -> dict:
    out: dict = {}
    if "control_metadata_list" in value:
        import capo_auditmanager.types.control_metadata_list

        out["controlMetadataList"] = (
            capo_auditmanager.types.control_metadata_list.serialize_json(
                value["control_metadata_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlsResponse:
    out: ListControlsResponse = {}  # type: ignore[typeddict-item]
    if "controlMetadataList" in data:
        import capo_auditmanager.types.control_metadata_list

        out["control_metadata_list"] = (
            capo_auditmanager.types.control_metadata_list.deserialize_json(
                data["controlMetadataList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
