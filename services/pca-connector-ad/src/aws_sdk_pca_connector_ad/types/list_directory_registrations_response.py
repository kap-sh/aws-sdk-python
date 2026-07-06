"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListDirectoryRegistrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.directory_registration_list
    import aws_sdk_pca_connector_ad.types.next_token


class ListDirectoryRegistrationsResponse(TypedDict, closed=True):
    directory_registrations: NotRequired[
        "aws_sdk_pca_connector_ad.types.directory_registration_list.DirectoryRegistrationList"
    ]
    """<p>Summary information about each directory registration you have created.</p>"""
    next_token: NotRequired["aws_sdk_pca_connector_ad.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDirectoryRegistrationsResponse) -> dict:
    out: dict = {}
    if "directory_registrations" in value:
        import aws_sdk_pca_connector_ad.types.directory_registration_list

        out["DirectoryRegistrations"] = (
            aws_sdk_pca_connector_ad.types.directory_registration_list.serialize_json(
                value["directory_registrations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDirectoryRegistrationsResponse:
    out: ListDirectoryRegistrationsResponse = {}  # type: ignore[typeddict-item]
    if "DirectoryRegistrations" in data:
        import aws_sdk_pca_connector_ad.types.directory_registration_list

        out["directory_registrations"] = (
            aws_sdk_pca_connector_ad.types.directory_registration_list.deserialize_json(
                data["DirectoryRegistrations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
