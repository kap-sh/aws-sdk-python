"""Generated from Smithy shape ``com.amazonaws.proton#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.max_page_results


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource for the listed tags.</p>"""
    next_token: NotRequired["str"]
    """<p>A token that indicates the location of the next resource tag in the array of resource tags, after the list of resource tags that was previously requested.</p>"""
    max_results: NotRequired["aws_sdk_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of tags to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
