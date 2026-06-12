"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteServerlessCacheResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.serverless_cache


class DeleteServerlessCacheResponse(TypedDict):
    serverless_cache: NotRequired[
        "aws_sdk_elasticache.types.serverless_cache.ServerlessCache"
    ]
    """<p>Provides the details of the specified serverless cache that is about to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServerlessCacheResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache" in value:
        import aws_sdk_elasticache.types.serverless_cache

        aws_sdk_elasticache.types.serverless_cache.serialize_query(
            value["serverless_cache"], pairs, f"{prefix}.ServerlessCache"
        )


def deserialize_query(el: Element) -> DeleteServerlessCacheResponse:
    out: DeleteServerlessCacheResponse = {}  # type: ignore[typeddict-item]
    child_serverless_cache = el.find("ServerlessCache")
    if child_serverless_cache is not None:
        import aws_sdk_elasticache.types.serverless_cache

        out["serverless_cache"] = (
            aws_sdk_elasticache.types.serverless_cache.deserialize_query(
                child_serverless_cache
            )
        )
    return out
