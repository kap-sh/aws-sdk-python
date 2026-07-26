"""Generated from Smithy shape ``com.amazonaws.s3tables#ListNamespacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.namespace_summary_list
    import capo_s3tables.types.next_token


class ListNamespacesResponse(TypedDict, closed=True):
    namespaces: "capo_s3tables.types.namespace_summary_list.NamespaceSummaryList"
    """<p>A list of namespaces.</p>"""
    continuation_token: NotRequired["capo_s3tables.types.next_token.NextToken"]
    """<p>The <code>ContinuationToken</code> for pagination of the list results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNamespacesResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.namespace_summary_list

    out["namespaces"] = capo_s3tables.types.namespace_summary_list.serialize_json(
        value["namespaces"]
    )
    if "continuation_token" in value:
        out["continuationToken"] = value["continuation_token"]
    return out


def deserialize_json(data: dict) -> ListNamespacesResponse:
    out: ListNamespacesResponse = {}  # type: ignore[typeddict-item]
    if "namespaces" in data:
        import capo_s3tables.types.namespace_summary_list

        out["namespaces"] = capo_s3tables.types.namespace_summary_list.deserialize_json(
            data["namespaces"]
        )
    else:
        raise DeserializationError("ListNamespacesResponse.namespaces required")
    if "continuationToken" in data:
        out["continuation_token"] = data["continuationToken"]
    return out
