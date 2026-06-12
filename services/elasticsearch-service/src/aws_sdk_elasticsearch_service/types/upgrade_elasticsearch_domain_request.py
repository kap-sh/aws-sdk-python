"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeElasticsearchDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.elasticsearch_version_string


class UpgradeElasticsearchDomainRequest(TypedDict):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    target_version: "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    """<p>The version of Elasticsearch that you intend to upgrade the domain to.</p>"""
    perform_check_only: NotRequired[
        "aws_sdk_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p> This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeElasticsearchDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["TargetVersion"] = value["target_version"]
    if "perform_check_only" in value:
        out["PerformCheckOnly"] = value["perform_check_only"]
    return out


def deserialize_json(data: dict) -> UpgradeElasticsearchDomainRequest:
    out: UpgradeElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "UpgradeElasticsearchDomainRequest.domain_name required"
        )
    if "TargetVersion" in data:
        out["target_version"] = data["TargetVersion"]
    else:
        raise DeserializationError(
            "UpgradeElasticsearchDomainRequest.target_version required"
        )
    if "PerformCheckOnly" in data:
        out["perform_check_only"] = data["PerformCheckOnly"]
    return out
