"""Generated from Smithy shape ``com.amazonaws.kendra#MemberUser``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.user_id


class MemberUser(TypedDict):
    user_id: "aws_sdk_kendra.types.user_id.UserId"
    """<p>The identifier of the user you want to map to a group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberUser) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MemberUser:
    out: MemberUser = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("MemberUser.user_id required")
    return out
