"""Generated from Smithy shape ``com.amazonaws.outposts#ListAssetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_type_list
    import aws_sdk_outposts.types.host_id_list
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.status_list
    import aws_sdk_outposts.types.token


class ListAssetsInput(TypedDict, closed=True):
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p> The ID or the Amazon Resource Name (ARN) of the Outpost. </p>"""
    host_id_filter: NotRequired["aws_sdk_outposts.types.host_id_list.HostIdList"]
    """<p>Filters the results by the host ID of a Dedicated Host.</p>"""
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    status_filter: NotRequired["aws_sdk_outposts.types.status_list.StatusList"]
    """<p>Filters the results by state.</p>"""
    asset_type_filter: NotRequired[
        "aws_sdk_outposts.types.asset_type_list.AssetTypeList"
    ]
    """<p>Filters the results by asset type.</p> <ul> <li> <p>COMPUTE - Server asset used for customer compute </p> </li> <li> <p>STORAGE - Server asset used by storage services </p> </li> <li> <p>POWERSHELF - Powershelf assets </p> </li> <li> <p>SWITCH - Switch assets </p> </li> <li> <p>NETWORKING - Asset managed by Amazon Web Services for networking purposes </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetsInput:
    out: ListAssetsInput = {}  # type: ignore[typeddict-item]
    return out
