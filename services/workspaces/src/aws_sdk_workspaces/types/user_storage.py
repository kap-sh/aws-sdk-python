"""Generated from Smithy shape ``com.amazonaws.workspaces#UserStorage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.non_empty_string


class UserStorage(TypedDict):
    capacity: "aws_sdk_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The size of the user volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStorage) -> dict:
    out: dict = {}
    out["Capacity"] = value["capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserStorage:
    out: UserStorage = {}  # type: ignore[typeddict-item]
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    else:
        raise DeserializationError("UserStorage.capacity required")
    return out
