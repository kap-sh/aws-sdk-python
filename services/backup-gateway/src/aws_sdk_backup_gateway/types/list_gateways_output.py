"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListGatewaysOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateways
    import aws_sdk_backup_gateway.types.next_token


class ListGatewaysOutput(TypedDict):
    gateways: NotRequired["aws_sdk_backup_gateway.types.gateways.Gateways"]
    """<p>A list of your gateways.</p>"""
    next_token: NotRequired["aws_sdk_backup_gateway.types.next_token.NextToken"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGatewaysOutput) -> dict:
    out: dict = {}
    if "gateways" in value:
        import aws_sdk_backup_gateway.types.gateways

        out["Gateways"] = aws_sdk_backup_gateway.types.gateways.serialize_aws_json_1_0(
            value["gateways"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGatewaysOutput:
    out: ListGatewaysOutput = {}  # type: ignore[typeddict-item]
    if "Gateways" in data:
        import aws_sdk_backup_gateway.types.gateways

        out["gateways"] = (
            aws_sdk_backup_gateway.types.gateways.deserialize_aws_json_1_0(
                data["Gateways"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
