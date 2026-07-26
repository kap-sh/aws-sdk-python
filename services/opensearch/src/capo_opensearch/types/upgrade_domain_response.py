"""Generated from Smithy shape ``com.amazonaws.opensearch#UpgradeDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.advanced_options
    import capo_opensearch.types.boolean
    import capo_opensearch.types.change_progress_details
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.string
    import capo_opensearch.types.version_string


class UpgradeDomainResponse(TypedDict, closed=True):
    upgrade_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The unique identifier of the domain upgrade.</p>"""
    domain_name: NotRequired["capo_opensearch.types.domain_name.DomainName"]
    """<p>The name of the domain that was upgraded.</p>"""
    target_version: NotRequired["capo_opensearch.types.version_string.VersionString"]
    """<p>OpenSearch or Elasticsearch version that the domain was upgraded to.</p>"""
    perform_check_only: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>When true, indicates that an upgrade eligibility check was performed.</p>"""
    advanced_options: NotRequired[
        "capo_opensearch.types.advanced_options.AdvancedOptions"
    ]
    """<p>The advanced options configuration for the domain.</p>"""
    change_progress_details: NotRequired[
        "capo_opensearch.types.change_progress_details.ChangeProgressDetails"
    ]
    """<p>Container for information about a configuration change happening on a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeDomainResponse) -> dict:
    out: dict = {}
    if "upgrade_id" in value:
        out["UpgradeId"] = value["upgrade_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "target_version" in value:
        out["TargetVersion"] = value["target_version"]
    if "perform_check_only" in value:
        out["PerformCheckOnly"] = value["perform_check_only"]
    if "advanced_options" in value:
        import capo_opensearch.types.advanced_options

        out["AdvancedOptions"] = capo_opensearch.types.advanced_options.serialize_json(
            value["advanced_options"]
        )
    if "change_progress_details" in value:
        import capo_opensearch.types.change_progress_details

        out["ChangeProgressDetails"] = (
            capo_opensearch.types.change_progress_details.serialize_json(
                value["change_progress_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpgradeDomainResponse:
    out: UpgradeDomainResponse = {}  # type: ignore[typeddict-item]
    if "UpgradeId" in data:
        out["upgrade_id"] = data["UpgradeId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "TargetVersion" in data:
        out["target_version"] = data["TargetVersion"]
    if "PerformCheckOnly" in data:
        out["perform_check_only"] = data["PerformCheckOnly"]
    if "AdvancedOptions" in data:
        import capo_opensearch.types.advanced_options

        out["advanced_options"] = (
            capo_opensearch.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if "ChangeProgressDetails" in data:
        import capo_opensearch.types.change_progress_details

        out["change_progress_details"] = (
            capo_opensearch.types.change_progress_details.deserialize_json(
                data["ChangeProgressDetails"]
            )
        )
    return out
