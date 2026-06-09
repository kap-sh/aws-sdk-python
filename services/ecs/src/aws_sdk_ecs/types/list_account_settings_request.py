"""Generated from Smithy shape ``com.amazonaws.ecs#ListAccountSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.setting_name
    import aws_sdk_ecs.types.string


class ListAccountSettingsRequest(TypedDict):
    name: NotRequired["aws_sdk_ecs.types.setting_name.SettingName"]
    """<p>The name of the account setting you want to list the settings for.</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The value of the account settings to filter results with. You must also specify an account setting name to use this parameter.</p>"""
    principal_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the principal, which can be a user, role, or the root user. If this field is omitted, the account settings are listed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p> <note> <p>Federated users assume the account setting of the root user and can't have explicit account settings set for them.</p> </note>"""
    effective_settings: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to return the effective settings. If <code>true</code>, the account settings for the root user or the default setting for the <code>principalArn</code> are returned. If <code>false</code>, the account settings for the <code>principalArn</code> are returned if they're set. Otherwise, no account settings are returned.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListAccountSettings</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: "aws_sdk_ecs.types.integer.Integer"
    """<p>The maximum number of account setting results returned by <code>ListAccountSettings</code> in paginated output. When this parameter is used, <code>ListAccountSettings</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAccountSettings</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 10. If this parameter isn't used, then <code>ListAccountSettings</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountSettingsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_ecs.types.setting_name

        out["name"] = aws_sdk_ecs.types.setting_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    out["effectiveSettings"] = value.get("effective_settings", False)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountSettingsRequest:
    out: ListAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_ecs.types.setting_name

        out["name"] = aws_sdk_ecs.types.setting_name.deserialize_aws_json_1_1(
            data["name"]
        )
    if "value" in data:
        out["value"] = data["value"]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    if "effectiveSettings" in data:
        out["effective_settings"] = data["effectiveSettings"]
    else:
        out["effective_settings"] = False
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    return out
