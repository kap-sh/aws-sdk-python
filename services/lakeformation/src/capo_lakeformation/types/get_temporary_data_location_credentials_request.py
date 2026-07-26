"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTemporaryDataLocationCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.audit_context
    import capo_lakeformation.types.credential_timeout_duration_second_integer
    import capo_lakeformation.types.credentials_scope
    import capo_lakeformation.types.path_string_list


class GetTemporaryDataLocationCredentialsRequest(TypedDict, closed=True):
    duration_seconds: NotRequired[
        "capo_lakeformation.types.credential_timeout_duration_second_integer.CredentialTimeoutDurationSecondInteger"
    ]
    """<p>The time period, between 900 and 43,200 seconds, for the timeout of the temporary credentials.</p>"""
    audit_context: NotRequired["capo_lakeformation.types.audit_context.AuditContext"]
    data_locations: NotRequired[
        "capo_lakeformation.types.path_string_list.PathStringList"
    ]
    """<p>The Amazon S3 data location that you want to access.</p>"""
    credentials_scope: NotRequired[
        "capo_lakeformation.types.credentials_scope.CredentialsScope"
    ]
    """<p>The credential scope is determined by the caller's Lake Formation permission on the associated table. Credential scope can be either:</p> <ul> <li> <p>READ - Provides read-only access to the data location.</p> </li> <li> <p>READ_WRITE - Provides both read and write access to the data location.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemporaryDataLocationCredentialsRequest) -> dict:
    out: dict = {}
    if "duration_seconds" in value:
        out["DurationSeconds"] = value["duration_seconds"]
    if "audit_context" in value:
        import capo_lakeformation.types.audit_context

        out["AuditContext"] = capo_lakeformation.types.audit_context.serialize_json(
            value["audit_context"]
        )
    if "data_locations" in value:
        import capo_lakeformation.types.path_string_list

        out["DataLocations"] = capo_lakeformation.types.path_string_list.serialize_json(
            value["data_locations"]
        )
    if "credentials_scope" in value:
        import capo_lakeformation.types.credentials_scope

        out["CredentialsScope"] = (
            capo_lakeformation.types.credentials_scope.serialize_json(
                value["credentials_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemporaryDataLocationCredentialsRequest:
    out: GetTemporaryDataLocationCredentialsRequest = {}  # type: ignore[typeddict-item]
    if "DurationSeconds" in data:
        out["duration_seconds"] = data["DurationSeconds"]
    if "AuditContext" in data:
        import capo_lakeformation.types.audit_context

        out["audit_context"] = capo_lakeformation.types.audit_context.deserialize_json(
            data["AuditContext"]
        )
    if "DataLocations" in data:
        import capo_lakeformation.types.path_string_list

        out["data_locations"] = (
            capo_lakeformation.types.path_string_list.deserialize_json(
                data["DataLocations"]
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
