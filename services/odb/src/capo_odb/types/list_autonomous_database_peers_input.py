"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabasePeersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class ListAutonomousDatabasePeersInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database whose peer databases you want to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabasePeersInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabasePeersInput:
    out: ListAutonomousDatabasePeersInput = {}  # type: ignore[typeddict-item]
    return out
