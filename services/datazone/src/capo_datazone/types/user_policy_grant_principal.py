"""Generated from Smithy shape ``com.amazonaws.datazone#UserPolicyGrantPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.all_users_grant_filter
    import capo_datazone.types.user_identifier


class _UserPolicyGrantPrincipal_userIdentifier(TypedDict, closed=True):
    userIdentifier: "capo_datazone.types.user_identifier.UserIdentifier"


class _UserPolicyGrantPrincipal_allUsersGrantFilter(TypedDict, closed=True):
    allUsersGrantFilter: (
        "capo_datazone.types.all_users_grant_filter.AllUsersGrantFilter"
    )


UserPolicyGrantPrincipal: TypeAlias = (
    _UserPolicyGrantPrincipal_userIdentifier
    | _UserPolicyGrantPrincipal_allUsersGrantFilter
)


# --- restJson1 ser/de ---
def serialize_json(value: UserPolicyGrantPrincipal) -> dict:
    if "userIdentifier" in value:
        return {"userIdentifier": value["userIdentifier"]}
    elif "allUsersGrantFilter" in value:
        import capo_datazone.types.all_users_grant_filter

        return {
            "allUsersGrantFilter": capo_datazone.types.all_users_grant_filter.serialize_json(
                value["allUsersGrantFilter"]
            )
        }
    else:
        raise SerializationError("UserPolicyGrantPrincipal: no variant present")


def deserialize_json(data: dict) -> UserPolicyGrantPrincipal:
    if "userIdentifier" in data:
        return {"userIdentifier": data["userIdentifier"]}
    elif "allUsersGrantFilter" in data:
        import capo_datazone.types.all_users_grant_filter

        return {
            "allUsersGrantFilter": capo_datazone.types.all_users_grant_filter.deserialize_json(
                data["allUsersGrantFilter"]
            )
        }
    else:
        raise DeserializationError(
            "UserPolicyGrantPrincipal: no recognized variant key"
        )
