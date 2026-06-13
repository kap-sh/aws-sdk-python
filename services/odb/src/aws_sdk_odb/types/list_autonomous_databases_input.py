"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabasesInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListAutonomousDatabasesInput(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabasesInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabasesInput:
    out: ListAutonomousDatabasesInput = {}  # type: ignore[typeddict-item]
    return out
