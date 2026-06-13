"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetDirectoryRegistrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.directory_registration


class GetDirectoryRegistrationResponse(TypedDict):
    directory_registration: NotRequired[
        "aws_sdk_pca_connector_ad.types.directory_registration.DirectoryRegistration"
    ]
    """<p>The directory registration represents the authorization of the connector service with a directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectoryRegistrationResponse) -> dict:
    out: dict = {}
    if "directory_registration" in value:
        import aws_sdk_pca_connector_ad.types.directory_registration

        out["DirectoryRegistration"] = (
            aws_sdk_pca_connector_ad.types.directory_registration.serialize_json(
                value["directory_registration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDirectoryRegistrationResponse:
    out: GetDirectoryRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "DirectoryRegistration" in data:
        import aws_sdk_pca_connector_ad.types.directory_registration

        out["directory_registration"] = (
            aws_sdk_pca_connector_ad.types.directory_registration.deserialize_json(
                data["DirectoryRegistration"]
            )
        )
    return out
