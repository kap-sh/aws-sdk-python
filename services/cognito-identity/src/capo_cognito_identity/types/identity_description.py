"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentityDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.date_type
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.logins_list


class IdentityDescription(TypedDict, closed=True):
    identity_id: NotRequired["capo_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    logins: NotRequired["capo_cognito_identity.types.logins_list.LoginsList"]
    """<p>The provider names.</p>"""
    creation_date: NotRequired["capo_cognito_identity.types.date_type.DateType"]
    """<p>Date on which the identity was created.</p>"""
    last_modified_date: NotRequired["capo_cognito_identity.types.date_type.DateType"]
    """<p>Date on which the identity was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityDescription) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "logins" in value:
        import capo_cognito_identity.types.logins_list

        out["Logins"] = capo_cognito_identity.types.logins_list.serialize_aws_json_1_1(
            value["logins"]
        )
    if "creation_date" in value:
        import capo_cognito_identity.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "last_modified_date" in value:
        import capo_cognito_identity.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityDescription:
    out: IdentityDescription = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "Logins" in data:
        import capo_cognito_identity.types.logins_list

        out["logins"] = (
            capo_cognito_identity.types.logins_list.deserialize_aws_json_1_1(
                data["Logins"]
            )
        )
    if "CreationDate" in data:
        import capo_cognito_identity.types.date_type

        out["creation_date"] = (
            capo_cognito_identity.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if "LastModifiedDate" in data:
        import capo_cognito_identity.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    return out
