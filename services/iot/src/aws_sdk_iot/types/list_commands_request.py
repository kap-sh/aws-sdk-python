"""Generated from Smithy shape ``com.amazonaws.iot#ListCommandsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_max_results
    import aws_sdk_iot.types.command_namespace
    import aws_sdk_iot.types.command_parameter_name
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.sort_order


class ListCommandsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_iot.types.command_max_results.CommandMaxResults"]
    """<p>The maximum number of results to return in this operation. By default, the API returns up to a maximum of 25 results. You can override this default value to return up to a maximum of 100 results for this operation.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>"""
    namespace: NotRequired["aws_sdk_iot.types.command_namespace.CommandNamespace"]
    """<p>The namespace of the command. By default, the API returns all commands that have been created for both <code>AWS-IoT</code> and <code>AWS-IoT-FleetWise</code> namespaces. You can override this default value if you want to return all commands that have been created only for a specific namespace.</p>"""
    command_parameter_name: NotRequired[
        "aws_sdk_iot.types.command_parameter_name.CommandParameterName"
    ]
    """<p>A filter that can be used to display the list of commands that have a specific command parameter name.</p>"""
    sort_order: NotRequired["aws_sdk_iot.types.sort_order.SortOrder"]
    """<p>Specify whether to list the commands that you have created in the ascending or descending order. By default, the API returns all commands in the descending order based on the time that they were created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommandsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCommandsRequest:
    out: ListCommandsRequest = {}  # type: ignore[typeddict-item]
    return out
