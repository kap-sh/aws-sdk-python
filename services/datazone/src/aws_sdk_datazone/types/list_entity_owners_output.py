"""Generated from Smithy shape ``com.amazonaws.datazone#ListEntityOwnersOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.entity_owners
    import aws_sdk_datazone.types.pagination_token


class ListEntityOwnersOutput(TypedDict):
    owners: "aws_sdk_datazone.types.entity_owners.EntityOwners"
    """<p>The owners of the entity.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntityOwnersOutput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.entity_owners

    out["owners"] = aws_sdk_datazone.types.entity_owners.serialize_json(value["owners"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntityOwnersOutput:
    out: ListEntityOwnersOutput = {}  # type: ignore[typeddict-item]
    if "owners" in data:
        import aws_sdk_datazone.types.entity_owners

        out["owners"] = aws_sdk_datazone.types.entity_owners.deserialize_json(
            data["owners"]
        )
    else:
        raise DeserializationError("ListEntityOwnersOutput.owners required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
