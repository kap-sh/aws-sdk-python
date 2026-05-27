"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedPrefixListAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_association_set
    import aws_sdk_ec2.types.string


class GetManagedPrefixListAssociationsResult(TypedDict):
    prefix_list_associations: NotRequired[
        "aws_sdk_ec2.types.prefix_list_association_set.PrefixListAssociationSet"
    ]
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
