"""Generated from Smithy shape ``com.amazonaws.deadline#ListFleetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_status
    import aws_sdk_deadline.types.identity_center_principal_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.resource_name


class ListFleetsRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the fleets.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    principal_id: NotRequired[
        "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    ]
    """<p>The principal ID of the members to include in the fleet.</p>"""
    display_name: NotRequired["aws_sdk_deadline.types.resource_name.ResourceName"]
    """<p>The display names of a list of fleets.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    status: NotRequired["aws_sdk_deadline.types.fleet_status.FleetStatus"]
    """<p>The status of the fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFleetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFleetsRequest:
    out: ListFleetsRequest = {}  # type: ignore[typeddict-item]
    return out
