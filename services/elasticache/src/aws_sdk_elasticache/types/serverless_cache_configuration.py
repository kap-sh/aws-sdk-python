"""Generated from Smithy shape ``com.amazonaws.elasticache#ServerlessCacheConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class ServerlessCacheConfiguration(TypedDict, closed=True):
    serverless_cache_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier of a serverless cache.</p>"""
    engine: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The engine that the serverless cache is configured with.</p>"""
    major_engine_version: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The engine version number that the serverless cache is configured with.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessCacheConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{prefix}.ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{prefix}.MajorEngineVersion", str(value["major_engine_version"]))
        )


def deserialize_query(el: Element) -> ServerlessCacheConfiguration:
    out: ServerlessCacheConfiguration = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    return out
