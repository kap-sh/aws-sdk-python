"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.regional_summary_list
    import aws_sdk_ec2.types.string


class AttributeSummary(TypedDict):
    attribute_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the attribute.</p>"""
    most_frequent_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The configuration value that is most frequently observed for the attribute.</p>"""
    number_of_matched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts with the same configuration value for the attribute that is most frequently observed.</p>"""
    number_of_unmatched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts with a configuration value different from the most frequently observed value for the attribute.</p>"""
    regional_summaries: NotRequired[
        "aws_sdk_ec2.types.regional_summary_list.RegionalSummaryList"
    ]
    """<p>The summary report for each Region for the attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttributeSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute_name" in value:
        pairs.append((f"{prefix}.AttributeName", str(value["attribute_name"])))
    if "most_frequent_value" in value:
        pairs.append((f"{prefix}.MostFrequentValue", str(value["most_frequent_value"])))
    if "number_of_matched_accounts" in value:
        pairs.append(
            (
                f"{prefix}.NumberOfMatchedAccounts",
                str(value["number_of_matched_accounts"]),
            )
        )
    if "number_of_unmatched_accounts" in value:
        pairs.append(
            (
                f"{prefix}.NumberOfUnmatchedAccounts",
                str(value["number_of_unmatched_accounts"]),
            )
        )
    if "regional_summaries" in value:
        import aws_sdk_ec2.types.regional_summary_list

        aws_sdk_ec2.types.regional_summary_list.serialize_ec2_query(
            value["regional_summaries"], pairs, f"{prefix}.RegionalSummarySet"
        )


def deserialize_ec2_query(el: Element) -> AttributeSummary:
    out: AttributeSummary = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_most_frequent_value = el.find("MostFrequentValue")
    if child_most_frequent_value is not None:
        out["most_frequent_value"] = str(child_most_frequent_value.text or "")
    child_number_of_matched_accounts = el.find("NumberOfMatchedAccounts")
    if child_number_of_matched_accounts is not None:
        out["number_of_matched_accounts"] = int(
            child_number_of_matched_accounts.text or ""
        )
    child_number_of_unmatched_accounts = el.find("NumberOfUnmatchedAccounts")
    if child_number_of_unmatched_accounts is not None:
        out["number_of_unmatched_accounts"] = int(
            child_number_of_unmatched_accounts.text or ""
        )
    if el.find("RegionalSummarySet") is not None:
        import aws_sdk_ec2.types.regional_summary_list

        out["regional_summaries"] = (
            aws_sdk_ec2.types.regional_summary_list.deserialize_ec2_query(
                el, "RegionalSummarySet"
            )
        )
    return out
