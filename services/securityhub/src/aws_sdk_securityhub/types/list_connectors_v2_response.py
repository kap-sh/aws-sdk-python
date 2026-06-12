"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConnectorsV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.connector_summary_list
    import aws_sdk_securityhub.types.next_token


class ListConnectorsV2Response(TypedDict):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""
    connectors: NotRequired[
        "aws_sdk_securityhub.types.connector_summary_list.ConnectorSummaryList"
    ]
    """<p>An array of connectorV2 summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsV2Response) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "connectors" in value:
        import aws_sdk_securityhub.types.connector_summary_list

        out["Connectors"] = (
            aws_sdk_securityhub.types.connector_summary_list.serialize_json(
                value["connectors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConnectorsV2Response:
    out: ListConnectorsV2Response = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Connectors" in data:
        import aws_sdk_securityhub.types.connector_summary_list

        out["connectors"] = (
            aws_sdk_securityhub.types.connector_summary_list.deserialize_json(
                data["Connectors"]
            )
        )
    return out
