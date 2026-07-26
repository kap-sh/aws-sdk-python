"""Generated from Smithy shape ``com.amazonaws.dsql#DeleteStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.client_token
    import capo_dsql.types.cluster_id
    import capo_dsql.types.stream_id


class DeleteStreamInput(TypedDict, closed=True):
    cluster_identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster containing the stream to delete.</p>"""
    stream_identifier: "capo_dsql.types.stream_id.StreamId"
    """<p>The ID of the stream to delete.</p>"""
    client_token: NotRequired["capo_dsql.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStreamInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteStreamInput:
    out: DeleteStreamInput = {}  # type: ignore[typeddict-item]
    return out
