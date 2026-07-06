"""Generated from Smithy shape ``com.amazonaws.connect#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.after_contact_work_configs
    import aws_sdk_connect.types.agent_username
    import aws_sdk_connect.types.auto_accept_configs
    import aws_sdk_connect.types.directory_user_id
    import aws_sdk_connect.types.hierarchy_group_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.password
    import aws_sdk_connect.types.persistent_connection_configs
    import aws_sdk_connect.types.phone_number_configs
    import aws_sdk_connect.types.routing_profile_id
    import aws_sdk_connect.types.security_profile_ids
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.user_identity_info
    import aws_sdk_connect.types.user_phone_config
    import aws_sdk_connect.types.voice_enhancement_configs


class CreateUserRequest(TypedDict, closed=True):
    username: "aws_sdk_connect.types.agent_username.AgentUsername"
    r"""<p>The user name for the account. For instances not using SAML for identity management, the user name can include up to 20 characters. If you are using SAML for identity management, the user name can include up to 64 characters from [a-zA-Z0-9_-.\@]+.</p> <p>Username can include @ only if used in an email format. For example:</p> <ul> <li> <p>Correct: testuser</p> </li> <li> <p>Correct: testuser@example.com</p> </li> <li> <p>Incorrect: testuser@example</p> </li> </ul>"""
    password: NotRequired["aws_sdk_connect.types.password.Password"]
    """<p>The password for the user account. A password is required if you are using Connect Customer for identity management. Otherwise, it is an error to include a password.</p>"""
    identity_info: NotRequired[
        "aws_sdk_connect.types.user_identity_info.UserIdentityInfo"
    ]
    """<p>The information about the identity of the user.</p>"""
    phone_config: NotRequired["aws_sdk_connect.types.user_phone_config.UserPhoneConfig"]
    """<p>The phone settings for the user. This parameter is optional. If not provided, the user can be configured using channel-specific parameters such as <code>AutoAcceptConfigs</code>, <code>AfterContactWorkConfigs</code>, <code>PhoneNumberConfigs</code>, <code>PersistentConnectionConfigs</code>, and <code>VoiceEnhancementConfigs</code>.</p>"""
    directory_user_id: NotRequired[
        "aws_sdk_connect.types.directory_user_id.DirectoryUserId"
    ]
    """<p>The identifier of the user account in the directory used for identity management. If Connect Customer cannot access the directory, you can specify this identifier to authenticate users. If you include the identifier, we assume that Connect Customer cannot access the directory. Otherwise, the identity information is used to authenticate users from your directory.</p> <p>This parameter is required if you are using an existing directory for identity management in Connect Customer when Connect Customer cannot access your directory to authenticate users. If you are using SAML for identity management and include this parameter, an error is returned.</p>"""
    security_profile_ids: (
        "aws_sdk_connect.types.security_profile_ids.SecurityProfileIds"
    )
    """<p>The identifier of the security profile for the user.</p>"""
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile for the user.</p>"""
    hierarchy_group_id: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the hierarchy group for the user.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    auto_accept_configs: NotRequired[
        "aws_sdk_connect.types.auto_accept_configs.AutoAcceptConfigs"
    ]
    """<p>The list of auto-accept configuration settings for each channel.</p>"""
    after_contact_work_configs: NotRequired[
        "aws_sdk_connect.types.after_contact_work_configs.AfterContactWorkConfigs"
    ]
    """<p>The list of after contact work (ACW) timeout configuration settings for each channel.</p>"""
    phone_number_configs: NotRequired[
        "aws_sdk_connect.types.phone_number_configs.PhoneNumberConfigs"
    ]
    """<p>The list of phone number configuration settings for each channel.</p>"""
    persistent_connection_configs: NotRequired[
        "aws_sdk_connect.types.persistent_connection_configs.PersistentConnectionConfigs"
    ]
    """<p>The list of persistent connection configuration settings for each channel.</p>"""
    voice_enhancement_configs: NotRequired[
        "aws_sdk_connect.types.voice_enhancement_configs.VoiceEnhancementConfigs"
    ]
    """<p>The list of voice enhancement configuration settings for each channel.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "identity_info" in value:
        import aws_sdk_connect.types.user_identity_info

        out["IdentityInfo"] = aws_sdk_connect.types.user_identity_info.serialize_json(
            value["identity_info"]
        )
    if "phone_config" in value:
        import aws_sdk_connect.types.user_phone_config

        out["PhoneConfig"] = aws_sdk_connect.types.user_phone_config.serialize_json(
            value["phone_config"]
        )
    if "directory_user_id" in value:
        out["DirectoryUserId"] = value["directory_user_id"]
    import aws_sdk_connect.types.security_profile_ids

    out["SecurityProfileIds"] = (
        aws_sdk_connect.types.security_profile_ids.serialize_json(
            value["security_profile_ids"]
        )
    )
    out["RoutingProfileId"] = value["routing_profile_id"]
    if "hierarchy_group_id" in value:
        out["HierarchyGroupId"] = value["hierarchy_group_id"]
    if "auto_accept_configs" in value:
        import aws_sdk_connect.types.auto_accept_configs

        out["AutoAcceptConfigs"] = (
            aws_sdk_connect.types.auto_accept_configs.serialize_json(
                value["auto_accept_configs"]
            )
        )
    if "after_contact_work_configs" in value:
        import aws_sdk_connect.types.after_contact_work_configs

        out["AfterContactWorkConfigs"] = (
            aws_sdk_connect.types.after_contact_work_configs.serialize_json(
                value["after_contact_work_configs"]
            )
        )
    if "phone_number_configs" in value:
        import aws_sdk_connect.types.phone_number_configs

        out["PhoneNumberConfigs"] = (
            aws_sdk_connect.types.phone_number_configs.serialize_json(
                value["phone_number_configs"]
            )
        )
    if "persistent_connection_configs" in value:
        import aws_sdk_connect.types.persistent_connection_configs

        out["PersistentConnectionConfigs"] = (
            aws_sdk_connect.types.persistent_connection_configs.serialize_json(
                value["persistent_connection_configs"]
            )
        )
    if "voice_enhancement_configs" in value:
        import aws_sdk_connect.types.voice_enhancement_configs

        out["VoiceEnhancementConfigs"] = (
            aws_sdk_connect.types.voice_enhancement_configs.serialize_json(
                value["voice_enhancement_configs"]
            )
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("CreateUserRequest.username required")
    if "Password" in data:
        out["password"] = data["Password"]
    if "IdentityInfo" in data:
        import aws_sdk_connect.types.user_identity_info

        out["identity_info"] = (
            aws_sdk_connect.types.user_identity_info.deserialize_json(
                data["IdentityInfo"]
            )
        )
    if "PhoneConfig" in data:
        import aws_sdk_connect.types.user_phone_config

        out["phone_config"] = aws_sdk_connect.types.user_phone_config.deserialize_json(
            data["PhoneConfig"]
        )
    if "DirectoryUserId" in data:
        out["directory_user_id"] = data["DirectoryUserId"]
    if "SecurityProfileIds" in data:
        import aws_sdk_connect.types.security_profile_ids

        out["security_profile_ids"] = (
            aws_sdk_connect.types.security_profile_ids.deserialize_json(
                data["SecurityProfileIds"]
            )
        )
    else:
        raise DeserializationError("CreateUserRequest.security_profile_ids required")
    if "RoutingProfileId" in data:
        out["routing_profile_id"] = data["RoutingProfileId"]
    else:
        raise DeserializationError("CreateUserRequest.routing_profile_id required")
    if "HierarchyGroupId" in data:
        out["hierarchy_group_id"] = data["HierarchyGroupId"]
    if "AutoAcceptConfigs" in data:
        import aws_sdk_connect.types.auto_accept_configs

        out["auto_accept_configs"] = (
            aws_sdk_connect.types.auto_accept_configs.deserialize_json(
                data["AutoAcceptConfigs"]
            )
        )
    if "AfterContactWorkConfigs" in data:
        import aws_sdk_connect.types.after_contact_work_configs

        out["after_contact_work_configs"] = (
            aws_sdk_connect.types.after_contact_work_configs.deserialize_json(
                data["AfterContactWorkConfigs"]
            )
        )
    if "PhoneNumberConfigs" in data:
        import aws_sdk_connect.types.phone_number_configs

        out["phone_number_configs"] = (
            aws_sdk_connect.types.phone_number_configs.deserialize_json(
                data["PhoneNumberConfigs"]
            )
        )
    if "PersistentConnectionConfigs" in data:
        import aws_sdk_connect.types.persistent_connection_configs

        out["persistent_connection_configs"] = (
            aws_sdk_connect.types.persistent_connection_configs.deserialize_json(
                data["PersistentConnectionConfigs"]
            )
        )
    if "VoiceEnhancementConfigs" in data:
        import aws_sdk_connect.types.voice_enhancement_configs

        out["voice_enhancement_configs"] = (
            aws_sdk_connect.types.voice_enhancement_configs.deserialize_json(
                data["VoiceEnhancementConfigs"]
            )
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
