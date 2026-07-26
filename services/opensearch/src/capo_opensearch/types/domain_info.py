"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.engine_type


class DomainInfo(TypedDict, closed=True):
    domain_name: NotRequired["capo_opensearch.types.domain_name.DomainName"]
    """<p>Name of the domain.</p>"""
    engine_type: NotRequired["capo_opensearch.types.engine_type.EngineType"]
    """<p>The type of search engine that the domain is running.<code>OpenSearch</code> for an OpenSearch engine, or <code>Elasticsearch</code> for a legacy Elasticsearch OSS engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainInfo) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "engine_type" in value:
        import capo_opensearch.types.engine_type

        out["EngineType"] = capo_opensearch.types.engine_type.serialize_json(
            value["engine_type"]
        )
    return out


def deserialize_json(data: dict) -> DomainInfo:
    out: DomainInfo = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "EngineType" in data:
        import capo_opensearch.types.engine_type

        out["engine_type"] = capo_opensearch.types.engine_type.deserialize_json(
            data["EngineType"]
        )
    return out
