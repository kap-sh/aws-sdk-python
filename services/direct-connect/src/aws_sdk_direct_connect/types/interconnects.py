"""Generated from Smithy shape ``com.amazonaws.directconnect#Interconnects``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.interconnect_list
    import aws_sdk_direct_connect.types.pagination_token


class Interconnects(TypedDict, closed=True):
    interconnects: NotRequired[
        "aws_sdk_direct_connect.types.interconnect_list.InterconnectList"
    ]
    """<p>The interconnects.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Interconnects) -> dict:
    out: dict = {}
    if "interconnects" in value:
        import aws_sdk_direct_connect.types.interconnect_list

        out["interconnects"] = (
            aws_sdk_direct_connect.types.interconnect_list.serialize_aws_json_1_1(
                value["interconnects"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Interconnects:
    out: Interconnects = {}  # type: ignore[typeddict-item]
    if "interconnects" in data:
        import aws_sdk_direct_connect.types.interconnect_list

        out["interconnects"] = (
            aws_sdk_direct_connect.types.interconnect_list.deserialize_aws_json_1_1(
                data["interconnects"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
