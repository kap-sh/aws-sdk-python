"""Generated from Smithy shape ``com.amazonaws.signin#PermissionStatementSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signin.types.permission_statement_summary

PermissionStatementSummaries: TypeAlias = list[
    "capo_signin.types.permission_statement_summary.PermissionStatementSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionStatementSummaries) -> list:
    import capo_signin.types.permission_statement_summary

    out: list = []
    for item in value:
        out.append(capo_signin.types.permission_statement_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionStatementSummaries:
    import capo_signin.types.permission_statement_summary

    out: PermissionStatementSummaries = []
    for item in data:
        out.append(
            capo_signin.types.permission_statement_summary.deserialize_json(item)
        )
    return out
