"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListTemplateGroupAccessControlEntriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.access_control_entry_list
    import capo_pca_connector_ad.types.next_token


class ListTemplateGroupAccessControlEntriesResponse(TypedDict, closed=True):
    access_control_entries: NotRequired[
        "capo_pca_connector_ad.types.access_control_entry_list.AccessControlEntryList"
    ]
    """<p>An access control entry grants or denies permission to an Active Directory group to enroll certificates for a template.</p>"""
    next_token: NotRequired["capo_pca_connector_ad.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateGroupAccessControlEntriesResponse) -> dict:
    out: dict = {}
    if "access_control_entries" in value:
        import capo_pca_connector_ad.types.access_control_entry_list

        out["AccessControlEntries"] = (
            capo_pca_connector_ad.types.access_control_entry_list.serialize_json(
                value["access_control_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplateGroupAccessControlEntriesResponse:
    out: ListTemplateGroupAccessControlEntriesResponse = {}  # type: ignore[typeddict-item]
    if "AccessControlEntries" in data:
        import capo_pca_connector_ad.types.access_control_entry_list

        out["access_control_entries"] = (
            capo_pca_connector_ad.types.access_control_entry_list.deserialize_json(
                data["AccessControlEntries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
