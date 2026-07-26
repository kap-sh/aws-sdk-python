"""Generated from Smithy shape ``com.amazonaws.connecthealth#UserContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.provider_role
    import capo_connecthealth.types.sensitive_non_empty_string
    import capo_connecthealth.types.specialty


class UserContext(TypedDict, closed=True):
    role: "capo_connecthealth.types.provider_role.ProviderRole"
    """<p/>"""
    user_id: (
        "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>Unique identifier of the user</p>"""
    specialty: NotRequired["capo_connecthealth.types.specialty.Specialty"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserContext) -> dict:
    out: dict = {}
    import capo_connecthealth.types.provider_role

    out["role"] = capo_connecthealth.types.provider_role.serialize_json(value["role"])
    out["userId"] = value["user_id"]
    if "specialty" in value:
        import capo_connecthealth.types.specialty

        out["specialty"] = capo_connecthealth.types.specialty.serialize_json(
            value["specialty"]
        )
    return out


def deserialize_json(data: dict) -> UserContext:
    out: UserContext = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import capo_connecthealth.types.provider_role

        out["role"] = capo_connecthealth.types.provider_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("UserContext.role required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UserContext.user_id required")
    if "specialty" in data:
        import capo_connecthealth.types.specialty

        out["specialty"] = capo_connecthealth.types.specialty.deserialize_json(
            data["specialty"]
        )
    return out
