"""Generated from Smithy shape ``com.amazonaws.backup#ListProtectedResourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.protected_resources_list
    import aws_sdk_backup.types.string


class ListProtectedResourcesOutput(TypedDict):
    results: NotRequired[
        "aws_sdk_backup.types.protected_resources_list.ProtectedResourcesList"
    ]
    """<p>An array of resources successfully backed up by Backup including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProtectedResourcesOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_backup.types.protected_resources_list

        out["Results"] = aws_sdk_backup.types.protected_resources_list.serialize_json(
            value["results"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProtectedResourcesOutput:
    out: ListProtectedResourcesOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_backup.types.protected_resources_list

        out["results"] = aws_sdk_backup.types.protected_resources_list.deserialize_json(
            data["Results"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
