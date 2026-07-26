"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetTemplateGroupAccessControlEntryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.access_control_entry


class GetTemplateGroupAccessControlEntryResponse(TypedDict, closed=True):
    access_control_entry: NotRequired[
        "capo_pca_connector_ad.types.access_control_entry.AccessControlEntry"
    ]
    """<p>An access control entry allows or denies an Active Directory group from enrolling and/or autoenrolling with a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateGroupAccessControlEntryResponse) -> dict:
    out: dict = {}
    if "access_control_entry" in value:
        import capo_pca_connector_ad.types.access_control_entry

        out["AccessControlEntry"] = (
            capo_pca_connector_ad.types.access_control_entry.serialize_json(
                value["access_control_entry"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemplateGroupAccessControlEntryResponse:
    out: GetTemplateGroupAccessControlEntryResponse = {}  # type: ignore[typeddict-item]
    if "AccessControlEntry" in data:
        import capo_pca_connector_ad.types.access_control_entry

        out["access_control_entry"] = (
            capo_pca_connector_ad.types.access_control_entry.deserialize_json(
                data["AccessControlEntry"]
            )
        )
    return out
