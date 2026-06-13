"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListPrivateConnectionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.private_connection_summary_list


class ListPrivateConnectionsOutput(TypedDict):
    private_connections: "aws_sdk_devops_agent.types.private_connection_summary_list.PrivateConnectionSummaryList"
    """<p>The list of Private Connections.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivateConnectionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.private_connection_summary_list

    out["privateConnections"] = (
        aws_sdk_devops_agent.types.private_connection_summary_list.serialize_json(
            value["private_connections"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListPrivateConnectionsOutput:
    out: ListPrivateConnectionsOutput = {}  # type: ignore[typeddict-item]
    if "privateConnections" in data:
        import aws_sdk_devops_agent.types.private_connection_summary_list

        out["private_connections"] = (
            aws_sdk_devops_agent.types.private_connection_summary_list.deserialize_json(
                data["privateConnections"]
            )
        )
    else:
        raise DeserializationError(
            "ListPrivateConnectionsOutput.private_connections required"
        )
    return out
