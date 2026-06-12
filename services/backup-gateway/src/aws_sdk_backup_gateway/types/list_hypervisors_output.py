"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListHypervisorsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.hypervisors
    import aws_sdk_backup_gateway.types.next_token


class ListHypervisorsOutput(TypedDict):
    hypervisors: NotRequired["aws_sdk_backup_gateway.types.hypervisors.Hypervisors"]
    """<p>A list of your <code>Hypervisor</code> objects, ordered by their Amazon Resource Names (ARNs).</p>"""
    next_token: NotRequired["aws_sdk_backup_gateway.types.next_token.NextToken"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListHypervisorsOutput) -> dict:
    out: dict = {}
    if "hypervisors" in value:
        import aws_sdk_backup_gateway.types.hypervisors

        out["Hypervisors"] = (
            aws_sdk_backup_gateway.types.hypervisors.serialize_aws_json_1_0(
                value["hypervisors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListHypervisorsOutput:
    out: ListHypervisorsOutput = {}  # type: ignore[typeddict-item]
    if "Hypervisors" in data:
        import aws_sdk_backup_gateway.types.hypervisors

        out["hypervisors"] = (
            aws_sdk_backup_gateway.types.hypervisors.deserialize_aws_json_1_0(
                data["Hypervisors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
