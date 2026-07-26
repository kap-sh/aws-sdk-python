"""Generated from Smithy shape ``com.amazonaws.glue#GetConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_list
    import capo_glue.types.token


class GetConnectionsResponse(TypedDict, closed=True):
    connection_list: NotRequired["capo_glue.types.connection_list.ConnectionList"]
    """<p>A list of requested connection definitions.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if the list of connections returned does not include the last of the filtered connections.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionsResponse) -> dict:
    out: dict = {}
    if "connection_list" in value:
        import capo_glue.types.connection_list

        out["ConnectionList"] = capo_glue.types.connection_list.serialize_aws_json_1_1(
            value["connection_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionsResponse:
    out: GetConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionList" in data:
        import capo_glue.types.connection_list

        out["connection_list"] = (
            capo_glue.types.connection_list.deserialize_aws_json_1_1(
                data["ConnectionList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
