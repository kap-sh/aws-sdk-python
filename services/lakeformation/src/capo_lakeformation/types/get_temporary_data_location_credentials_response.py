"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTemporaryDataLocationCredentialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.credentials_scope
    import capo_lakeformation.types.path_string_list
    import capo_lakeformation.types.temporary_credentials


class GetTemporaryDataLocationCredentialsResponse(TypedDict, closed=True):
    credentials: NotRequired[
        "capo_lakeformation.types.temporary_credentials.TemporaryCredentials"
    ]
    accessible_data_locations: NotRequired[
        "capo_lakeformation.types.path_string_list.PathStringList"
    ]
    """<p>Refers to the Amazon S3 locations that can be accessed through the <code>GetTemporaryCredentialsForLocation</code> API operation.</p>"""
    credentials_scope: NotRequired[
        "capo_lakeformation.types.credentials_scope.CredentialsScope"
    ]
    """<p>The credential scope is determined by the caller's Lake Formation permission on the associated table. Credential scope can be either:</p> <ul> <li> <p>READ - Provides read-only access to the data location.</p> </li> <li> <p>READ_WRITE - Provides both read and write access to the data location.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemporaryDataLocationCredentialsResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_lakeformation.types.temporary_credentials

        out["Credentials"] = (
            capo_lakeformation.types.temporary_credentials.serialize_json(
                value["credentials"]
            )
        )
    if "accessible_data_locations" in value:
        import capo_lakeformation.types.path_string_list

        out["AccessibleDataLocations"] = (
            capo_lakeformation.types.path_string_list.serialize_json(
                value["accessible_data_locations"]
            )
        )
    if "credentials_scope" in value:
        import capo_lakeformation.types.credentials_scope

        out["CredentialsScope"] = (
            capo_lakeformation.types.credentials_scope.serialize_json(
                value["credentials_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemporaryDataLocationCredentialsResponse:
    out: GetTemporaryDataLocationCredentialsResponse = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import capo_lakeformation.types.temporary_credentials

        out["credentials"] = (
            capo_lakeformation.types.temporary_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    if "AccessibleDataLocations" in data:
        import capo_lakeformation.types.path_string_list

        out["accessible_data_locations"] = (
            capo_lakeformation.types.path_string_list.deserialize_json(
                data["AccessibleDataLocations"]
            )
        )
    if "CredentialsScope" in data:
        import capo_lakeformation.types.credentials_scope

        out["credentials_scope"] = (
            capo_lakeformation.types.credentials_scope.deserialize_json(
                data["CredentialsScope"]
            )
        )
    return out
