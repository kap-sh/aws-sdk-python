"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#AccessRights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.access_right


class AccessRights(TypedDict, closed=True):
    enroll: NotRequired["capo_pca_connector_ad.types.access_right.AccessRight"]
    """<p>Allow or deny an Active Directory group from enrolling certificates issued against a template.</p>"""
    auto_enroll: NotRequired["capo_pca_connector_ad.types.access_right.AccessRight"]
    """<p>Allow or deny an Active Directory group from autoenrolling certificates issued against a template. The Active Directory group must be allowed to enroll to allow autoenrollment</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessRights) -> dict:
    out: dict = {}
    if "enroll" in value:
        import capo_pca_connector_ad.types.access_right

        out["Enroll"] = capo_pca_connector_ad.types.access_right.serialize_json(
            value["enroll"]
        )
    if "auto_enroll" in value:
        import capo_pca_connector_ad.types.access_right

        out["AutoEnroll"] = capo_pca_connector_ad.types.access_right.serialize_json(
            value["auto_enroll"]
        )
    return out


def deserialize_json(data: dict) -> AccessRights:
    out: AccessRights = {}  # type: ignore[typeddict-item]
    if "Enroll" in data:
        import capo_pca_connector_ad.types.access_right

        out["enroll"] = capo_pca_connector_ad.types.access_right.deserialize_json(
            data["Enroll"]
        )
    if "AutoEnroll" in data:
        import capo_pca_connector_ad.types.access_right

        out["auto_enroll"] = capo_pca_connector_ad.types.access_right.deserialize_json(
            data["AutoEnroll"]
        )
    return out
