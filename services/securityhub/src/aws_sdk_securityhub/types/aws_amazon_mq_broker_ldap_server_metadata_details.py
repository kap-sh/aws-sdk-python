"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerLdapServerMetadataDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsAmazonMqBrokerLdapServerMetadataDetails(TypedDict):
    hosts: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> Specifies the location of the LDAP server, such as Amazon Web Services Directory Service for Microsoft Active Directory. </p>"""
    role_base: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The distinguished name of the node in the directory information tree (DIT) to search for roles or groups. </p>"""
    role_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The group name attribute in a role entry whose value is the name of that role. </p>"""
    role_search_matching: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The LDAP search filter used to find roles within the <code>roleBase</code>. </p>"""
    role_search_subtree: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> The directory search scope for the role. If set to <code>true</code>, the scope is to search the entire subtree. </p>"""
    service_account_username: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A username for the service account, which is an account in your LDAP server that has access to initiate a connection. </p>"""
    user_base: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Selects a particular subtree of the directory information tree (DIT) to search for user entries. </p>"""
    user_role_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the LDAP attribute in the user's directory entry for the user's group membership. </p>"""
    user_search_matching: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The LDAP search filter used to find users within the <code>userBase</code>. </p>"""
    user_search_subtree: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> The directory search scope for the user. If set to true, the scope is to search the entire subtree. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerLdapServerMetadataDetails) -> dict:
    out: dict = {}
    if "hosts" in value:
        import aws_sdk_securityhub.types.string_list

        out["Hosts"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["hosts"]
        )
    if "role_base" in value:
        out["RoleBase"] = value["role_base"]
    if "role_name" in value:
        out["RoleName"] = value["role_name"]
    if "role_search_matching" in value:
        out["RoleSearchMatching"] = value["role_search_matching"]
    if "role_search_subtree" in value:
        out["RoleSearchSubtree"] = value["role_search_subtree"]
    if "service_account_username" in value:
        out["ServiceAccountUsername"] = value["service_account_username"]
    if "user_base" in value:
        out["UserBase"] = value["user_base"]
    if "user_role_name" in value:
        out["UserRoleName"] = value["user_role_name"]
    if "user_search_matching" in value:
        out["UserSearchMatching"] = value["user_search_matching"]
    if "user_search_subtree" in value:
        out["UserSearchSubtree"] = value["user_search_subtree"]
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerLdapServerMetadataDetails:
    out: AwsAmazonMqBrokerLdapServerMetadataDetails = {}  # type: ignore[typeddict-item]
    if "Hosts" in data:
        import aws_sdk_securityhub.types.string_list

        out["hosts"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["Hosts"]
        )
    if "RoleBase" in data:
        out["role_base"] = data["RoleBase"]
    if "RoleName" in data:
        out["role_name"] = data["RoleName"]
    if "RoleSearchMatching" in data:
        out["role_search_matching"] = data["RoleSearchMatching"]
    if "RoleSearchSubtree" in data:
        out["role_search_subtree"] = data["RoleSearchSubtree"]
    if "ServiceAccountUsername" in data:
        out["service_account_username"] = data["ServiceAccountUsername"]
    if "UserBase" in data:
        out["user_base"] = data["UserBase"]
    if "UserRoleName" in data:
        out["user_role_name"] = data["UserRoleName"]
    if "UserSearchMatching" in data:
        out["user_search_matching"] = data["UserSearchMatching"]
    if "UserSearchSubtree" in data:
        out["user_search_subtree"] = data["UserSearchSubtree"]
    return out
