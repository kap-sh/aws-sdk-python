"""Generated from Smithy shape ``com.amazonaws.ec2#RegionalSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class RegionalSummary(TypedDict):
    region_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region.</p>"""
    number_of_matched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts in the Region with the same configuration value for the attribute that is most frequently observed.</p>"""
    number_of_unmatched_accounts: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accounts in the Region with a configuration value different from the most frequently observed value for the attribute.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegionalSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "region_name" in value:
        pairs.append((f"{prefix}.RegionName", str(value["region_name"])))
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


def deserialize_ec2_query(el: Element) -> RegionalSummary:
    out: RegionalSummary = {}  # type: ignore[typeddict-item]
    child_region_name = el.find("RegionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
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
    return out
