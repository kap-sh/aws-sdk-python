"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConfigurationPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.configuration_policy_summary_list
    import capo_securityhub.types.next_token


class ListConfigurationPoliciesResponse(TypedDict, closed=True):
    configuration_policy_summaries: NotRequired[
        "capo_securityhub.types.configuration_policy_summary_list.ConfigurationPolicySummaryList"
    ]
    """<p> Provides metadata for each of your configuration policies. </p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p> The <code>NextToken</code> value to include in the next <code>ListConfigurationPolicies</code> request. When the results of a <code>ListConfigurationPolicies</code> request exceed <code>MaxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationPoliciesResponse) -> dict:
    out: dict = {}
    if "configuration_policy_summaries" in value:
        import capo_securityhub.types.configuration_policy_summary_list

        out["ConfigurationPolicySummaries"] = (
            capo_securityhub.types.configuration_policy_summary_list.serialize_json(
                value["configuration_policy_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationPoliciesResponse:
    out: ListConfigurationPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicySummaries" in data:
        import capo_securityhub.types.configuration_policy_summary_list

        out["configuration_policy_summaries"] = (
            capo_securityhub.types.configuration_policy_summary_list.deserialize_json(
                data["ConfigurationPolicySummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
