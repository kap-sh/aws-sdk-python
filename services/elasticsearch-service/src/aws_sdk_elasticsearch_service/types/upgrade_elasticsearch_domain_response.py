"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeElasticsearchDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.change_progress_details
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.elasticsearch_version_string


class UpgradeElasticsearchDomainResponse(TypedDict, closed=True):
    domain_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    ]
    target_version: NotRequired[
        "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    ]
    """<p>The version of Elasticsearch that you intend to upgrade the domain to.</p>"""
    perform_check_only: NotRequired[
        "aws_sdk_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p> This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade. </p>"""
    change_progress_details: NotRequired[
        "aws_sdk_elasticsearch_service.types.change_progress_details.ChangeProgressDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeElasticsearchDomainResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "target_version" in value:
        out["TargetVersion"] = value["target_version"]
    if "perform_check_only" in value:
        out["PerformCheckOnly"] = value["perform_check_only"]
    if "change_progress_details" in value:
        import aws_sdk_elasticsearch_service.types.change_progress_details

        out["ChangeProgressDetails"] = (
            aws_sdk_elasticsearch_service.types.change_progress_details.serialize_json(
                value["change_progress_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpgradeElasticsearchDomainResponse:
    out: UpgradeElasticsearchDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "TargetVersion" in data:
        out["target_version"] = data["TargetVersion"]
    if "PerformCheckOnly" in data:
        out["perform_check_only"] = data["PerformCheckOnly"]
    if "ChangeProgressDetails" in data:
        import aws_sdk_elasticsearch_service.types.change_progress_details

        out["change_progress_details"] = (
            aws_sdk_elasticsearch_service.types.change_progress_details.deserialize_json(
                data["ChangeProgressDetails"]
            )
        )
    return out
