"""Generated from Smithy shape ``com.amazonaws.keyspaces#ListKeyspacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_summary_list
    import capo_keyspaces.types.next_token


class ListKeyspacesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_keyspaces.types.next_token.NextToken"]
    """<p>A token to specify where to start paginating. This is the <code>NextToken</code> from a previously truncated response.</p>"""
    keyspaces: "capo_keyspaces.types.keyspace_summary_list.KeyspaceSummaryList"
    """<p>A list of keyspaces.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListKeyspacesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_keyspaces.types.keyspace_summary_list

    out["keyspaces"] = (
        capo_keyspaces.types.keyspace_summary_list.serialize_aws_json_1_0(
            value["keyspaces"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListKeyspacesResponse:
    out: ListKeyspacesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "keyspaces" in data:
        import capo_keyspaces.types.keyspace_summary_list

        out["keyspaces"] = (
            capo_keyspaces.types.keyspace_summary_list.deserialize_aws_json_1_0(
                data["keyspaces"]
            )
        )
    else:
        raise DeserializationError("ListKeyspacesResponse.keyspaces required")
    return out
