"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.engine_type


class DomainInfo(TypedDict, closed=True):
    domain_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    ]
    """<p> Specifies the <code>DomainName</code>.</p>"""
    engine_type: NotRequired[
        "aws_sdk_elasticsearch_service.types.engine_type.EngineType"
    ]
    """<p> Specifies the <code>EngineType</code> of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainInfo) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "engine_type" in value:
        import aws_sdk_elasticsearch_service.types.engine_type

        out["EngineType"] = (
            aws_sdk_elasticsearch_service.types.engine_type.serialize_json(
                value["engine_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainInfo:
    out: DomainInfo = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "EngineType" in data:
        import aws_sdk_elasticsearch_service.types.engine_type

        out["engine_type"] = (
            aws_sdk_elasticsearch_service.types.engine_type.deserialize_json(
                data["EngineType"]
            )
        )
    return out
