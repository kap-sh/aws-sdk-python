"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListResourcesForTagOptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.resource_type
    import capo_service_catalog.types.tag_option_id


class ListResourcesForTagOptionInput(TypedDict, closed=True):
    tag_option_id: "capo_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""
    resource_type: NotRequired["capo_service_catalog.types.resource_type.ResourceType"]
    """<p>The resource type.</p> <ul> <li> <p> <code>Portfolio</code> </p> </li> <li> <p> <code>Product</code> </p> </li> </ul>"""
    page_size: "capo_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForTagOptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForTagOptionInput:
    out: ListResourcesForTagOptionInput = {}  # type: ignore[typeddict-item]
    return out
