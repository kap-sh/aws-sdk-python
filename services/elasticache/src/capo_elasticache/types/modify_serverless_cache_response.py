"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyServerlessCacheResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.serverless_cache


class ModifyServerlessCacheResponse(TypedDict, closed=True):
    serverless_cache: NotRequired[
        "capo_elasticache.types.serverless_cache.ServerlessCache"
    ]
    """<p>The response for the attempt to modify the serverless cache.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyServerlessCacheResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache" in value:
        import capo_elasticache.types.serverless_cache

        capo_elasticache.types.serverless_cache.serialize_query(
            value["serverless_cache"], pairs, f"{prefix}.ServerlessCache"
        )


def deserialize_query(el: Element) -> ModifyServerlessCacheResponse:
    out: ModifyServerlessCacheResponse = {}  # type: ignore[typeddict-item]
    child_serverless_cache = el.find("ServerlessCache")
    if child_serverless_cache is not None:
        import capo_elasticache.types.serverless_cache

        out["serverless_cache"] = (
            capo_elasticache.types.serverless_cache.deserialize_query(
                child_serverless_cache
            )
        )
    return out
