"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ListPlatformVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_summary_list
    import capo_elastic_beanstalk.types.token


class ListPlatformVersionsResult(TypedDict, closed=True):
    platform_summary_list: NotRequired[
        "capo_elastic_beanstalk.types.platform_summary_list.PlatformSummaryList"
    ]
    """<p>Summary information about the platform versions.</p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.token.Token"]
    """<p>In a paginated request, if this value isn't <code>null</code>, it's the token that you can pass in a subsequent request to get the next response page.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPlatformVersionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_summary_list" in value:
        import capo_elastic_beanstalk.types.platform_summary_list

        capo_elastic_beanstalk.types.platform_summary_list.serialize_query(
            value["platform_summary_list"], pairs, f"{prefix}.PlatformSummaryList"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPlatformVersionsResult:
    out: ListPlatformVersionsResult = {}  # type: ignore[typeddict-item]
    child_platform_summary_list = el.find("PlatformSummaryList")
    if child_platform_summary_list is not None:
        import capo_elastic_beanstalk.types.platform_summary_list

        out["platform_summary_list"] = (
            capo_elastic_beanstalk.types.platform_summary_list.deserialize_query(
                child_platform_summary_list
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
