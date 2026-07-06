"""Generated from Smithy shape ``com.amazonaws.outposts#ListCatalogItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.catalog_item_class_list
    import aws_sdk_outposts.types.ec2_family_list
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.supported_storage_list
    import aws_sdk_outposts.types.token


class ListCatalogItemsInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    item_class_filter: NotRequired[
        "aws_sdk_outposts.types.catalog_item_class_list.CatalogItemClassList"
    ]
    """<p>Filters the results by item class.</p>"""
    supported_storage_filter: NotRequired[
        "aws_sdk_outposts.types.supported_storage_list.SupportedStorageList"
    ]
    """<p>Filters the results by storage option.</p>"""
    ec2_family_filter: NotRequired[
        "aws_sdk_outposts.types.ec2_family_list.EC2FamilyList"
    ]
    """<p>Filters the results by EC2 family (for example, M5).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCatalogItemsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCatalogItemsInput:
    out: ListCatalogItemsInput = {}  # type: ignore[typeddict-item]
    return out
