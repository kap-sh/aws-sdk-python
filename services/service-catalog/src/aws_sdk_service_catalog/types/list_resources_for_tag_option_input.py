"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListResourcesForTagOptionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.resource_type
    import aws_sdk_service_catalog.types.tag_option_id


class ListResourcesForTagOptionInput(TypedDict):
    tag_option_id: "aws_sdk_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""
    resource_type: NotRequired[
        "aws_sdk_service_catalog.types.resource_type.ResourceType"
    ]
    """<p>The resource type.</p> <ul> <li> <p> <code>Portfolio</code> </p> </li> <li> <p> <code>Product</code> </p> </li> </ul>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForTagOptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForTagOptionInput:
    out: ListResourcesForTagOptionInput = {}  # type: ignore[typeddict-item]
    return out
