"""Generated from Smithy shape ``com.amazonaws.workmail#GetPersonalAccessTokenMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.personal_access_token_id
    import capo_workmail.types.personal_access_token_name
    import capo_workmail.types.personal_access_token_scope_list
    import capo_workmail.types.timestamp
    import capo_workmail.types.work_mail_identifier


class GetPersonalAccessTokenMetadataResponse(TypedDict, closed=True):
    personal_access_token_id: NotRequired[
        "capo_workmail.types.personal_access_token_id.PersonalAccessTokenId"
    ]
    """<p> The Personal Access Token ID.</p>"""
    user_id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p> The WorkMail User ID. </p>"""
    name: NotRequired[
        "capo_workmail.types.personal_access_token_name.PersonalAccessTokenName"
    ]
    """<p> The Personal Access Token name. </p>"""
    date_created: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p> The date when the Personal Access Token ID was created. </p>"""
    date_last_used: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p> The date when the Personal Access Token ID was last used. </p>"""
    expires_time: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p> The time when the Personal Access Token ID will expire. </p>"""
    scopes: NotRequired[
        "capo_workmail.types.personal_access_token_scope_list.PersonalAccessTokenScopeList"
    ]
    """<p> Lists all the Personal Access Token permissions for a mailbox. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPersonalAccessTokenMetadataResponse) -> dict:
    out: dict = {}
    if "personal_access_token_id" in value:
        out["PersonalAccessTokenId"] = value["personal_access_token_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "date_created" in value:
        import capo_workmail.types.timestamp

        out["DateCreated"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_last_used" in value:
        import capo_workmail.types.timestamp

        out["DateLastUsed"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_last_used"]
        )
    if "expires_time" in value:
        import capo_workmail.types.timestamp

        out["ExpiresTime"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["expires_time"]
        )
    if "scopes" in value:
        import capo_workmail.types.personal_access_token_scope_list

        out["Scopes"] = (
            capo_workmail.types.personal_access_token_scope_list.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPersonalAccessTokenMetadataResponse:
    out: GetPersonalAccessTokenMetadataResponse = {}  # type: ignore[typeddict-item]
    if "PersonalAccessTokenId" in data:
        out["personal_access_token_id"] = data["PersonalAccessTokenId"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DateCreated" in data:
        import capo_workmail.types.timestamp

        out["date_created"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateLastUsed" in data:
        import capo_workmail.types.timestamp

        out["date_last_used"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateLastUsed"]
        )
    if "ExpiresTime" in data:
        import capo_workmail.types.timestamp

        out["expires_time"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["ExpiresTime"]
        )
    if "Scopes" in data:
        import capo_workmail.types.personal_access_token_scope_list

        out["scopes"] = (
            capo_workmail.types.personal_access_token_scope_list.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    return out
