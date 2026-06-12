"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateServerlessCacheResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.serverless_cache


class CreateServerlessCacheResponse(TypedDict):
    serverless_cache: NotRequired[
        "aws_sdk_elasticache.types.serverless_cache.ServerlessCache"
    ]
    """<p>The response for the attempt to create the serverless cache.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServerlessCacheResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache" in value:
        import aws_sdk_elasticache.types.serverless_cache

        aws_sdk_elasticache.types.serverless_cache.serialize_query(
            value["serverless_cache"], pairs, f"{prefix}.ServerlessCache"
        )


def deserialize_query(el: Element) -> CreateServerlessCacheResponse:
    out: CreateServerlessCacheResponse = {}  # type: ignore[typeddict-item]
    child_serverless_cache = el.find("ServerlessCache")
    if child_serverless_cache is not None:
        import aws_sdk_elasticache.types.serverless_cache

        out["serverless_cache"] = (
            aws_sdk_elasticache.types.serverless_cache.deserialize_query(
                child_serverless_cache
            )
        )
    return out
