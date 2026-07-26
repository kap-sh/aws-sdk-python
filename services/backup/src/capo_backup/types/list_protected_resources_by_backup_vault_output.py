"""Generated from Smithy shape ``com.amazonaws.backup#ListProtectedResourcesByBackupVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.protected_resources_list
    import capo_backup.types.string


class ListProtectedResourcesByBackupVaultOutput(TypedDict, closed=True):
    results: NotRequired[
        "capo_backup.types.protected_resources_list.ProtectedResourcesList"
    ]
    """<p>These are the results returned for the request ListProtectedResourcesByBackupVault.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProtectedResourcesByBackupVaultOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_backup.types.protected_resources_list

        out["Results"] = capo_backup.types.protected_resources_list.serialize_json(
            value["results"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProtectedResourcesByBackupVaultOutput:
    out: ListProtectedResourcesByBackupVaultOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_backup.types.protected_resources_list

        out["results"] = capo_backup.types.protected_resources_list.deserialize_json(
            data["Results"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
