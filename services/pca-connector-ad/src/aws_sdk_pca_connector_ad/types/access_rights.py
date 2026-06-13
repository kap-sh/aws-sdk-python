"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#AccessRights``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.access_right


class AccessRights(TypedDict):
    enroll: NotRequired["aws_sdk_pca_connector_ad.types.access_right.AccessRight"]
    """<p>Allow or deny an Active Directory group from enrolling certificates issued against a template.</p>"""
    auto_enroll: NotRequired["aws_sdk_pca_connector_ad.types.access_right.AccessRight"]
    """<p>Allow or deny an Active Directory group from autoenrolling certificates issued against a template. The Active Directory group must be allowed to enroll to allow autoenrollment</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessRights) -> dict:
    out: dict = {}
    if "enroll" in value:
        import aws_sdk_pca_connector_ad.types.access_right

        out["Enroll"] = aws_sdk_pca_connector_ad.types.access_right.serialize_json(
            value["enroll"]
        )
    if "auto_enroll" in value:
        import aws_sdk_pca_connector_ad.types.access_right

        out["AutoEnroll"] = aws_sdk_pca_connector_ad.types.access_right.serialize_json(
            value["auto_enroll"]
        )
    return out


def deserialize_json(data: dict) -> AccessRights:
    out: AccessRights = {}  # type: ignore[typeddict-item]
    if "Enroll" in data:
        import aws_sdk_pca_connector_ad.types.access_right

        out["enroll"] = aws_sdk_pca_connector_ad.types.access_right.deserialize_json(
            data["Enroll"]
        )
    if "AutoEnroll" in data:
        import aws_sdk_pca_connector_ad.types.access_right

        out["auto_enroll"] = (
            aws_sdk_pca_connector_ad.types.access_right.deserialize_json(
                data["AutoEnroll"]
            )
        )
    return out
