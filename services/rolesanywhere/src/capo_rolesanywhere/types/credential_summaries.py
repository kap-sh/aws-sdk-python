"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CredentialSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.credential_summary

CredentialSummaries: TypeAlias = list[
    "capo_rolesanywhere.types.credential_summary.CredentialSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialSummaries) -> list:
    import capo_rolesanywhere.types.credential_summary

    out: list = []
    for item in value:
        out.append(capo_rolesanywhere.types.credential_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CredentialSummaries:
    import capo_rolesanywhere.types.credential_summary

    out: CredentialSummaries = []
    for item in data:
        out.append(capo_rolesanywhere.types.credential_summary.deserialize_json(item))
    return out
