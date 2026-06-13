"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentConnectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.connector_list
    import aws_sdk_evs.types.pagination_token


class ListEnvironmentConnectorsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for next page results. Make the call again using this token to retrieve the next page.</p>"""
    connectors: NotRequired["aws_sdk_evs.types.connector_list.ConnectorList"]
    """<p>A list of connectors in the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentConnectorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "connectors" in value:
        import aws_sdk_evs.types.connector_list

        out["connectors"] = aws_sdk_evs.types.connector_list.serialize_aws_json_1_0(
            value["connectors"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentConnectorsResponse:
    out: ListEnvironmentConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "connectors" in data:
        import aws_sdk_evs.types.connector_list

        out["connectors"] = aws_sdk_evs.types.connector_list.deserialize_aws_json_1_0(
            data["connectors"]
        )
    return out
