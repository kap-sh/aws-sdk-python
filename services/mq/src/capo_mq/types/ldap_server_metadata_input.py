"""Generated from Smithy shape ``com.amazonaws.mq#LdapServerMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__boolean
    import capo_mq.types.__list_of__string
    import capo_mq.types.__string


class LdapServerMetadataInput(TypedDict, closed=True):
    hosts: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>Specifies the location of the LDAP server such as Directory Service for Microsoft Active Directory. Optional failover server.</p>"""
    role_base: NotRequired["capo_mq.types.__string.__string"]
    """<p>The distinguished name of the node in the directory information tree (DIT) to search for roles or groups. For example, ou=group, ou=corp, dc=corp, dc=example, dc=com.</p>"""
    role_name: NotRequired["capo_mq.types.__string.__string"]
    """<p>Specifies the LDAP attribute that identifies the group name attribute in the object returned from the group membership query.</p>"""
    role_search_matching: NotRequired["capo_mq.types.__string.__string"]
    """<p>The LDAP search filter used to find roles within the roleBase. The distinguished name of the user matched by userSearchMatching is substituted into the {0} placeholder in the search filter. The client's username is substituted into the {1} placeholder. For example, if you set this option to (member=uid={1})for the user janedoe, the search filter becomes (member=uid=janedoe) after string substitution. It matches all role entries that have a member attribute equal to uid=janedoe under the subtree selected by the roleBase.</p>"""
    role_search_subtree: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>The directory search scope for the role. If set to true, scope is to search the entire subtree.</p>"""
    service_account_password: NotRequired["capo_mq.types.__string.__string"]
    """<p>Service account password. A service account is an account in your LDAP server that has access to initiate a connection. For example, cn=admin,dc=corp, dc=example, dc=com.</p>"""
    service_account_username: NotRequired["capo_mq.types.__string.__string"]
    """<p>Service account username. A service account is an account in your LDAP server that has access to initiate a connection. For example, cn=admin,dc=corp, dc=example, dc=com.</p>"""
    user_base: NotRequired["capo_mq.types.__string.__string"]
    """<p>Select a particular subtree of the directory information tree (DIT) to search for user entries. The subtree is specified by a DN, which specifies the base node of the subtree. For example, by setting this option to ou=Users,ou=corp, dc=corp, dc=example, dc=com, the search for user entries is restricted to the subtree beneath ou=Users, ou=corp, dc=corp, dc=example, dc=com.</p>"""
    user_role_name: NotRequired["capo_mq.types.__string.__string"]
    """<p>Specifies the name of the LDAP attribute for the user group membership.</p>"""
    user_search_matching: NotRequired["capo_mq.types.__string.__string"]
    """<p>The LDAP search filter used to find users within the userBase. The client's username is substituted into the {0} placeholder in the search filter. For example, if this option is set to (uid={0}) and the received username is janedoe, the search filter becomes (uid=janedoe) after string substitution. It will result in matching an entry like uid=janedoe, ou=Users,ou=corp, dc=corp, dc=example, dc=com.</p>"""
    user_search_subtree: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>The directory search scope for the user. If set to true, scope is to search the entire subtree.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LdapServerMetadataInput) -> dict:
    out: dict = {}
    if "hosts" in value:
        import capo_mq.types.__list_of__string

        out["hosts"] = capo_mq.types.__list_of__string.serialize_json(value["hosts"])
    if "role_base" in value:
        out["roleBase"] = value["role_base"]
    if "role_name" in value:
        out["roleName"] = value["role_name"]
    if "role_search_matching" in value:
        out["roleSearchMatching"] = value["role_search_matching"]
    if "role_search_subtree" in value:
        out["roleSearchSubtree"] = value["role_search_subtree"]
    if "service_account_password" in value:
        out["serviceAccountPassword"] = value["service_account_password"]
    if "service_account_username" in value:
        out["serviceAccountUsername"] = value["service_account_username"]
    if "user_base" in value:
        out["userBase"] = value["user_base"]
    if "user_role_name" in value:
        out["userRoleName"] = value["user_role_name"]
    if "user_search_matching" in value:
        out["userSearchMatching"] = value["user_search_matching"]
    if "user_search_subtree" in value:
        out["userSearchSubtree"] = value["user_search_subtree"]
    return out


def deserialize_json(data: dict) -> LdapServerMetadataInput:
    out: LdapServerMetadataInput = {}  # type: ignore[typeddict-item]
    if "hosts" in data:
        import capo_mq.types.__list_of__string

        out["hosts"] = capo_mq.types.__list_of__string.deserialize_json(data["hosts"])
    if "roleBase" in data:
        out["role_base"] = data["roleBase"]
    if "roleName" in data:
        out["role_name"] = data["roleName"]
    if "roleSearchMatching" in data:
        out["role_search_matching"] = data["roleSearchMatching"]
    if "roleSearchSubtree" in data:
        out["role_search_subtree"] = data["roleSearchSubtree"]
    if "serviceAccountPassword" in data:
        out["service_account_password"] = data["serviceAccountPassword"]
    if "serviceAccountUsername" in data:
        out["service_account_username"] = data["serviceAccountUsername"]
    if "userBase" in data:
        out["user_base"] = data["userBase"]
    if "userRoleName" in data:
        out["user_role_name"] = data["userRoleName"]
    if "userSearchMatching" in data:
        out["user_search_matching"] = data["userSearchMatching"]
    if "userSearchSubtree" in data:
        out["user_search_subtree"] = data["userSearchSubtree"]
    return out
