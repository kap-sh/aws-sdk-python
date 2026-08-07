"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeAccountLimitsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account_limit_list
    import capo_cloudformation.types.next_token


class DescribeAccountLimitsOutput(TypedDict, closed=True):
    account_limits: NotRequired[
        "capo_cloudformation.types.account_limit_list.AccountLimitList"
    ]
    """<p>An account limit structure that contain a list of CloudFormation account limits and their values.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountLimitsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "account_limits" in value:
        import capo_cloudformation.types.account_limit_list

        capo_cloudformation.types.account_limit_list.serialize_query(
            value["account_limits"], pairs, f"{key_prefix}AccountLimits"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAccountLimitsOutput:
    out: DescribeAccountLimitsOutput = {}  # type: ignore[typeddict-item]
    child_account_limits = el.find("AccountLimits")
    if child_account_limits is not None:
        import capo_cloudformation.types.account_limit_list

        out["account_limits"] = (
            capo_cloudformation.types.account_limit_list.deserialize_query(
                child_account_limits
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
