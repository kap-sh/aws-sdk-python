"""Generated from Smithy shape ``com.amazonaws.wafv2#ListAvailableManagedRuleGroupVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.managed_rule_group_versions
    import aws_sdk_wafv2.types.next_marker
    import aws_sdk_wafv2.types.version_key_string


class ListAvailableManagedRuleGroupVersionsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    versions: NotRequired[
        "aws_sdk_wafv2.types.managed_rule_group_versions.ManagedRuleGroupVersions"
    ]
    """<p>The versions that are currently available for the specified managed rule group. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""
    current_default_version: NotRequired[
        "aws_sdk_wafv2.types.version_key_string.VersionKeyString"
    ]
    """<p>The name of the version that's currently set as the default. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListAvailableManagedRuleGroupVersionsResponse,
) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "versions" in value:
        import aws_sdk_wafv2.types.managed_rule_group_versions

        out["Versions"] = (
            aws_sdk_wafv2.types.managed_rule_group_versions.serialize_aws_json_1_1(
                value["versions"]
            )
        )
    if "current_default_version" in value:
        out["CurrentDefaultVersion"] = value["current_default_version"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListAvailableManagedRuleGroupVersionsResponse:
    out: ListAvailableManagedRuleGroupVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Versions" in data:
        import aws_sdk_wafv2.types.managed_rule_group_versions

        out["versions"] = (
            aws_sdk_wafv2.types.managed_rule_group_versions.deserialize_aws_json_1_1(
                data["Versions"]
            )
        )
    if "CurrentDefaultVersion" in data:
        out["current_default_version"] = data["CurrentDefaultVersion"]
    return out
