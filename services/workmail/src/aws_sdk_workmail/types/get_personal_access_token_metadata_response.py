"""Generated from Smithy shape ``com.amazonaws.workmail#GetPersonalAccessTokenMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.personal_access_token_id
    import aws_sdk_workmail.types.personal_access_token_name
    import aws_sdk_workmail.types.personal_access_token_scope_list
    import aws_sdk_workmail.types.timestamp
    import aws_sdk_workmail.types.work_mail_identifier


class GetPersonalAccessTokenMetadataResponse(TypedDict, closed=True):
    personal_access_token_id: NotRequired[
        "aws_sdk_workmail.types.personal_access_token_id.PersonalAccessTokenId"
    ]
    """<p> The Personal Access Token ID.</p>"""
    user_id: NotRequired[
        "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p> The WorkMail User ID. </p>"""
    name: NotRequired[
        "aws_sdk_workmail.types.personal_access_token_name.PersonalAccessTokenName"
    ]
    """<p> The Personal Access Token name. </p>"""
    date_created: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p> The date when the Personal Access Token ID was created. </p>"""
    date_last_used: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p> The date when the Personal Access Token ID was last used. </p>"""
    expires_time: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p> The time when the Personal Access Token ID will expire. </p>"""
    scopes: NotRequired[
        "aws_sdk_workmail.types.personal_access_token_scope_list.PersonalAccessTokenScopeList"
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
        import aws_sdk_workmail.types.timestamp

        out["DateCreated"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_last_used" in value:
        import aws_sdk_workmail.types.timestamp

        out["DateLastUsed"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_last_used"]
        )
    if "expires_time" in value:
        import aws_sdk_workmail.types.timestamp

        out["ExpiresTime"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["expires_time"]
        )
    if "scopes" in value:
        import aws_sdk_workmail.types.personal_access_token_scope_list

        out["Scopes"] = (
            aws_sdk_workmail.types.personal_access_token_scope_list.serialize_aws_json_1_1(
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
        import aws_sdk_workmail.types.timestamp

        out["date_created"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateLastUsed" in data:
        import aws_sdk_workmail.types.timestamp

        out["date_last_used"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["DateLastUsed"]
            )
        )
    if "ExpiresTime" in data:
        import aws_sdk_workmail.types.timestamp

        out["expires_time"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["ExpiresTime"]
        )
    if "Scopes" in data:
        import aws_sdk_workmail.types.personal_access_token_scope_list

        out["scopes"] = (
            aws_sdk_workmail.types.personal_access_token_scope_list.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    return out
