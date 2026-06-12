"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetTagKeysInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.pagination_token


class GetTagKeysInput(TypedDict):
    pagination_token: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagKeysInput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagKeysInput:
    out: GetTagKeysInput = {}  # type: ignore[typeddict-item]
    if "PaginationToken" in data:
        out["pagination_token"] = data["PaginationToken"]
    return out
