"""Generated from Smithy shape ``com.amazonaws.outposts#ListAssetInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.account_id_list
    import aws_sdk_outposts.types.asset_id_list
    import aws_sdk_outposts.types.aws_service_name_list
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.outpost_instance_type_list
    import aws_sdk_outposts.types.token


class ListAssetInstancesInput(TypedDict, closed=True):
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID of the Outpost.</p>"""
    asset_id_filter: NotRequired["aws_sdk_outposts.types.asset_id_list.AssetIdList"]
    """<p>Filters the results by asset ID.</p>"""
    instance_type_filter: NotRequired[
        "aws_sdk_outposts.types.outpost_instance_type_list.OutpostInstanceTypeList"
    ]
    """<p>Filters the results by instance ID.</p>"""
    account_id_filter: NotRequired[
        "aws_sdk_outposts.types.account_id_list.AccountIdList"
    ]
    """<p>Filters the results by account ID.</p>"""
    aws_service_filter: NotRequired[
        "aws_sdk_outposts.types.aws_service_name_list.AWSServiceNameList"
    ]
    """<p>Filters the results by Amazon Web Services service.</p>"""
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetInstancesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetInstancesInput:
    out: ListAssetInstancesInput = {}  # type: ignore[typeddict-item]
    return out
