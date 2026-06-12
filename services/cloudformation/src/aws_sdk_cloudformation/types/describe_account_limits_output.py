"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeAccountLimitsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.account_limit_list
    import aws_sdk_cloudformation.types.next_token


class DescribeAccountLimitsOutput(TypedDict):
    account_limits: NotRequired[
        "aws_sdk_cloudformation.types.account_limit_list.AccountLimitList"
    ]
    """<p>An account limit structure that contain a list of CloudFormation account limits and their values.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountLimitsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_limits" in value:
        import aws_sdk_cloudformation.types.account_limit_list

        aws_sdk_cloudformation.types.account_limit_list.serialize_query(
            value["account_limits"], pairs, f"{prefix}.AccountLimits"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAccountLimitsOutput:
    out: DescribeAccountLimitsOutput = {}  # type: ignore[typeddict-item]
    child_account_limits = el.find("AccountLimits")
    if child_account_limits is not None:
        import aws_sdk_cloudformation.types.account_limit_list

        out["account_limits"] = (
            aws_sdk_cloudformation.types.account_limit_list.deserialize_query(
                child_account_limits
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
