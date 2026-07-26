"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetDirectoryRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.directory_registration


class GetDirectoryRegistrationResponse(TypedDict, closed=True):
    directory_registration: NotRequired[
        "capo_pca_connector_ad.types.directory_registration.DirectoryRegistration"
    ]
    """<p>The directory registration represents the authorization of the connector service with a directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectoryRegistrationResponse) -> dict:
    out: dict = {}
    if "directory_registration" in value:
        import capo_pca_connector_ad.types.directory_registration

        out["DirectoryRegistration"] = (
            capo_pca_connector_ad.types.directory_registration.serialize_json(
                value["directory_registration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDirectoryRegistrationResponse:
    out: GetDirectoryRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "DirectoryRegistration" in data:
        import capo_pca_connector_ad.types.directory_registration

        out["directory_registration"] = (
            capo_pca_connector_ad.types.directory_registration.deserialize_json(
                data["DirectoryRegistration"]
            )
        )
    return out
