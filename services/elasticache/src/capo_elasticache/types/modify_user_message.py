"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyUserMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.access_string
    import capo_elasticache.types.authentication_mode
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.engine_type
    import capo_elasticache.types.password_list_input
    import capo_elasticache.types.user_id


class ModifyUserMessage(TypedDict, closed=True):
    user_id: NotRequired["capo_elasticache.types.user_id.UserId"]
    """<p>The ID of the user.</p>"""
    access_string: NotRequired["capo_elasticache.types.access_string.AccessString"]
    """<p>Access permissions string used for this user.</p>"""
    append_access_string: NotRequired[
        "capo_elasticache.types.access_string.AccessString"
    ]
    """<p>Adds additional user permissions to the access string.</p>"""
    passwords: NotRequired[
        "capo_elasticache.types.password_list_input.PasswordListInput"
    ]
    """<p>The passwords belonging to the user. You are allowed up to two.</p>"""
    no_password_required: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates no password is required for the user.</p>"""
    authentication_mode: NotRequired[
        "capo_elasticache.types.authentication_mode.AuthenticationMode"
    ]
    """<p>Specifies how to authenticate the user.</p>"""
    engine: NotRequired["capo_elasticache.types.engine_type.EngineType"]
    """<p>Modifies the engine listed for a user. The options are valkey or redis.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyUserMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_id" in value:
        pairs.append((f"{key_prefix}UserId", str(value["user_id"])))
    if "access_string" in value:
        pairs.append((f"{key_prefix}AccessString", str(value["access_string"])))
    if "append_access_string" in value:
        pairs.append(
            (f"{key_prefix}AppendAccessString", str(value["append_access_string"]))
        )
    if "passwords" in value:
        import capo_elasticache.types.password_list_input

        capo_elasticache.types.password_list_input.serialize_query(
            value["passwords"], pairs, f"{key_prefix}Passwords"
        )
    if "no_password_required" in value:
        pairs.append(
            (
                f"{key_prefix}NoPasswordRequired",
                "true" if value["no_password_required"] else "false",
            )
        )
    if "authentication_mode" in value:
        import capo_elasticache.types.authentication_mode

        capo_elasticache.types.authentication_mode.serialize_query(
            value["authentication_mode"], pairs, f"{key_prefix}AuthenticationMode"
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))


def deserialize_query(el: Element) -> ModifyUserMessage:
    out: ModifyUserMessage = {}  # type: ignore[typeddict-item]
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_access_string = el.find("AccessString")
    if child_access_string is not None:
        out["access_string"] = str(child_access_string.text or "")
    child_append_access_string = el.find("AppendAccessString")
    if child_append_access_string is not None:
        out["append_access_string"] = str(child_append_access_string.text or "")
    child_passwords = el.find("Passwords")
    if child_passwords is not None:
        import capo_elasticache.types.password_list_input

        out["passwords"] = capo_elasticache.types.password_list_input.deserialize_query(
            child_passwords
        )
    child_no_password_required = el.find("NoPasswordRequired")
    if child_no_password_required is not None:
        out["no_password_required"] = (
            child_no_password_required.text or ""
        ).lower() == "true"
    child_authentication_mode = el.find("AuthenticationMode")
    if child_authentication_mode is not None:
        import capo_elasticache.types.authentication_mode

        out["authentication_mode"] = (
            capo_elasticache.types.authentication_mode.deserialize_query(
                child_authentication_mode
            )
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    return out
