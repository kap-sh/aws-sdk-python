"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.user_type


class UserReference(TypedDict, closed=True):
    user_id: "str"
    """<p>The unique identifier for the user</p>"""
    user_type: "aws_sdk_devops_agent.types.user_type.UserType"
    """<p>The type of user</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserReference) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    import aws_sdk_devops_agent.types.user_type

    out["userType"] = aws_sdk_devops_agent.types.user_type.serialize_json(
        value["user_type"]
    )
    return out


def deserialize_json(data: dict) -> UserReference:
    out: UserReference = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UserReference.user_id required")
    if "userType" in data:
        import aws_sdk_devops_agent.types.user_type

        out["user_type"] = aws_sdk_devops_agent.types.user_type.deserialize_json(
            data["userType"]
        )
    else:
        raise DeserializationError("UserReference.user_type required")
    return out
