"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListNamespacesRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListNamespacesRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListNamespaces</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListNamespaces</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNamespacesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNamespacesRequest:
    out: ListNamespacesRequest = {}  # type: ignore[typeddict-item]
    return out
