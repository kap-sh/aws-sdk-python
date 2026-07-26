"""Generated from Smithy shape ``com.amazonaws.iot#DeleteRoleAliasResponse``."""

from typing_extensions import TypedDict


class DeleteRoleAliasResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoleAliasResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoleAliasResponse:
    out: DeleteRoleAliasResponse = {}  # type: ignore[typeddict-item]
    return out
