"""Generated from Smithy shape ``com.amazonaws.securityagent#UserConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.user_role


class UserConfig(TypedDict, closed=True):
    role: NotRequired["aws_sdk_securityagent.types.user_role.UserRole"]
    """<p>The role assigned to the user. Currently, only MEMBER is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserConfig) -> dict:
    out: dict = {}
    if "role" in value:
        import aws_sdk_securityagent.types.user_role

        out["role"] = aws_sdk_securityagent.types.user_role.serialize_json(
            value["role"]
        )
    return out


def deserialize_json(data: dict) -> UserConfig:
    out: UserConfig = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import aws_sdk_securityagent.types.user_role

        out["role"] = aws_sdk_securityagent.types.user_role.deserialize_json(
            data["role"]
        )
    return out
