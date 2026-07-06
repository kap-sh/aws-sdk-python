"""Generated from Smithy shape ``com.amazonaws.connecthealth#UserContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.provider_role
    import aws_sdk_connecthealth.types.sensitive_non_empty_string
    import aws_sdk_connecthealth.types.specialty


class UserContext(TypedDict, closed=True):
    role: "aws_sdk_connecthealth.types.provider_role.ProviderRole"
    """<p/>"""
    user_id: (
        "aws_sdk_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>Unique identifier of the user</p>"""
    specialty: NotRequired["aws_sdk_connecthealth.types.specialty.Specialty"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserContext) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.provider_role

    out["role"] = aws_sdk_connecthealth.types.provider_role.serialize_json(
        value["role"]
    )
    out["userId"] = value["user_id"]
    if "specialty" in value:
        import aws_sdk_connecthealth.types.specialty

        out["specialty"] = aws_sdk_connecthealth.types.specialty.serialize_json(
            value["specialty"]
        )
    return out


def deserialize_json(data: dict) -> UserContext:
    out: UserContext = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import aws_sdk_connecthealth.types.provider_role

        out["role"] = aws_sdk_connecthealth.types.provider_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("UserContext.role required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UserContext.user_id required")
    if "specialty" in data:
        import aws_sdk_connecthealth.types.specialty

        out["specialty"] = aws_sdk_connecthealth.types.specialty.deserialize_json(
            data["specialty"]
        )
    return out
