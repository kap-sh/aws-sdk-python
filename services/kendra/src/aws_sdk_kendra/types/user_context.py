"""Generated from Smithy shape ``com.amazonaws.kendra#UserContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_groups
    import aws_sdk_kendra.types.groups
    import aws_sdk_kendra.types.principal_name
    import aws_sdk_kendra.types.token


class UserContext(TypedDict, closed=True):
    token: NotRequired["aws_sdk_kendra.types.token.Token"]
    """<p>The user context token for filtering search results for a user. It must be a JWT or a JSON token.</p>"""
    user_id: NotRequired["aws_sdk_kendra.types.principal_name.PrincipalName"]
    """<p>The identifier of the user you want to filter search results based on their access to documents.</p>"""
    groups: NotRequired["aws_sdk_kendra.types.groups.Groups"]
    """<p>The list of groups you want to filter search results based on the groups' access to documents.</p>"""
    data_source_groups: NotRequired[
        "aws_sdk_kendra.types.data_source_groups.DataSourceGroups"
    ]
    """<p>The list of data source groups you want to filter search results based on groups' access to documents in that data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserContext) -> dict:
    out: dict = {}
    if "token" in value:
        out["Token"] = value["token"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "groups" in value:
        import aws_sdk_kendra.types.groups

        out["Groups"] = aws_sdk_kendra.types.groups.serialize_aws_json_1_1(
            value["groups"]
        )
    if "data_source_groups" in value:
        import aws_sdk_kendra.types.data_source_groups

        out["DataSourceGroups"] = (
            aws_sdk_kendra.types.data_source_groups.serialize_aws_json_1_1(
                value["data_source_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserContext:
    out: UserContext = {}  # type: ignore[typeddict-item]
    if "Token" in data:
        out["token"] = data["Token"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "Groups" in data:
        import aws_sdk_kendra.types.groups

        out["groups"] = aws_sdk_kendra.types.groups.deserialize_aws_json_1_1(
            data["Groups"]
        )
    if "DataSourceGroups" in data:
        import aws_sdk_kendra.types.data_source_groups

        out["data_source_groups"] = (
            aws_sdk_kendra.types.data_source_groups.deserialize_aws_json_1_1(
                data["DataSourceGroups"]
            )
        )
    return out
