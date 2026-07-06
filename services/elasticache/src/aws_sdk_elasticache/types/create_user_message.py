"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateUserMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.access_string
    import aws_sdk_elasticache.types.authentication_mode
    import aws_sdk_elasticache.types.boolean_optional
    import aws_sdk_elasticache.types.engine_type
    import aws_sdk_elasticache.types.password_list_input
    import aws_sdk_elasticache.types.tag_list
    import aws_sdk_elasticache.types.user_id
    import aws_sdk_elasticache.types.user_name


class CreateUserMessage(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_elasticache.types.user_id.UserId"]
    """<p>The ID of the user. This value is stored as a lowercase string.</p>"""
    user_name: NotRequired["aws_sdk_elasticache.types.user_name.UserName"]
    """<p>The username of the user.</p>"""
    engine: NotRequired["aws_sdk_elasticache.types.engine_type.EngineType"]
    """<p>The options are valkey or redis. </p>"""
    passwords: NotRequired[
        "aws_sdk_elasticache.types.password_list_input.PasswordListInput"
    ]
    """<p>Passwords used for this user. You can create up to two passwords for each user.</p>"""
    access_string: NotRequired["aws_sdk_elasticache.types.access_string.AccessString"]
    """<p>Access permissions string used for this user.</p>"""
    no_password_required: NotRequired[
        "aws_sdk_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates a password is not required for this user.</p>"""
    tags: NotRequired["aws_sdk_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""
    authentication_mode: NotRequired[
        "aws_sdk_elasticache.types.authentication_mode.AuthenticationMode"
    ]
    """<p>Specifies how to authenticate the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateUserMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "passwords" in value:
        import aws_sdk_elasticache.types.password_list_input

        aws_sdk_elasticache.types.password_list_input.serialize_query(
            value["passwords"], pairs, f"{prefix}.Passwords"
        )
    if "access_string" in value:
        pairs.append((f"{prefix}.AccessString", str(value["access_string"])))
    if "no_password_required" in value:
        pairs.append(
            (
                f"{prefix}.NoPasswordRequired",
                "true" if value["no_password_required"] else "false",
            )
        )
    if "tags" in value:
        import aws_sdk_elasticache.types.tag_list

        aws_sdk_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "authentication_mode" in value:
        import aws_sdk_elasticache.types.authentication_mode

        aws_sdk_elasticache.types.authentication_mode.serialize_query(
            value["authentication_mode"], pairs, f"{prefix}.AuthenticationMode"
        )


def deserialize_query(el: Element) -> CreateUserMessage:
    out: CreateUserMessage = {}  # type: ignore[typeddict-item]
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_passwords = el.find("Passwords")
    if child_passwords is not None:
        import aws_sdk_elasticache.types.password_list_input

        out["passwords"] = (
            aws_sdk_elasticache.types.password_list_input.deserialize_query(
                child_passwords
            )
        )
    child_access_string = el.find("AccessString")
    if child_access_string is not None:
        out["access_string"] = str(child_access_string.text or "")
    child_no_password_required = el.find("NoPasswordRequired")
    if child_no_password_required is not None:
        out["no_password_required"] = (
            child_no_password_required.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elasticache.types.tag_list

        out["tags"] = aws_sdk_elasticache.types.tag_list.deserialize_query(child_tags)
    child_authentication_mode = el.find("AuthenticationMode")
    if child_authentication_mode is not None:
        import aws_sdk_elasticache.types.authentication_mode

        out["authentication_mode"] = (
            aws_sdk_elasticache.types.authentication_mode.deserialize_query(
                child_authentication_mode
            )
        )
    return out
