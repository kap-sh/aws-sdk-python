"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConfigurationPolicyAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.configuration_policy_association_summary_list
    import aws_sdk_securityhub.types.next_token


class ListConfigurationPolicyAssociationsResponse(TypedDict):
    configuration_policy_association_summaries: NotRequired[
        "aws_sdk_securityhub.types.configuration_policy_association_summary_list.ConfigurationPolicyAssociationSummaryList"
    ]
    """<p> An object that contains the details of each configuration policy association that’s returned in a <code>ListConfigurationPolicyAssociations</code> request. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> The <code>NextToken</code> value to include in the next <code>ListConfigurationPolicyAssociations</code> request. When the results of a <code>ListConfigurationPolicyAssociations</code> request exceed <code>MaxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationPolicyAssociationsResponse) -> dict:
    out: dict = {}
    if "configuration_policy_association_summaries" in value:
        import aws_sdk_securityhub.types.configuration_policy_association_summary_list

        out["ConfigurationPolicyAssociationSummaries"] = (
            aws_sdk_securityhub.types.configuration_policy_association_summary_list.serialize_json(
                value["configuration_policy_association_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationPolicyAssociationsResponse:
    out: ListConfigurationPolicyAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationPolicyAssociationSummaries" in data:
        import aws_sdk_securityhub.types.configuration_policy_association_summary_list

        out["configuration_policy_association_summaries"] = (
            aws_sdk_securityhub.types.configuration_policy_association_summary_list.deserialize_json(
                data["ConfigurationPolicyAssociationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
