"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ListPlatformBranchesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.platform_branch_summary_list
    import aws_sdk_elastic_beanstalk.types.token


class ListPlatformBranchesResult(TypedDict, closed=True):
    platform_branch_summary_list: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_branch_summary_list.PlatformBranchSummaryList"
    ]
    """<p>Summary information about the platform branches.</p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.token.Token"]
    """<p>In a paginated request, if this value isn't <code>null</code>, it's the token that you can pass in a subsequent request to get the next response page.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPlatformBranchesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_branch_summary_list" in value:
        import aws_sdk_elastic_beanstalk.types.platform_branch_summary_list

        aws_sdk_elastic_beanstalk.types.platform_branch_summary_list.serialize_query(
            value["platform_branch_summary_list"],
            pairs,
            f"{prefix}.PlatformBranchSummaryList",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPlatformBranchesResult:
    out: ListPlatformBranchesResult = {}  # type: ignore[typeddict-item]
    child_platform_branch_summary_list = el.find("PlatformBranchSummaryList")
    if child_platform_branch_summary_list is not None:
        import aws_sdk_elastic_beanstalk.types.platform_branch_summary_list

        out["platform_branch_summary_list"] = (
            aws_sdk_elastic_beanstalk.types.platform_branch_summary_list.deserialize_query(
                child_platform_branch_summary_list
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
