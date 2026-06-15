"""Generated from Smithy shape ``com.amazonaws.eventbridge#AppSyncParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.graph_ql_operation


class AppSyncParameters(TypedDict):
    graph_ql_operation: NotRequired[
        "aws_sdk_eventbridge.types.graph_ql_operation.GraphQLOperation"
    ]
    r"""<p>The GraphQL operation; that is, the query, mutation, or subscription to be parsed and executed by the GraphQL service.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appsync/latest/devguide/graphql-architecture.html#graphql-operations\">Operations</a> in the <i>AppSync User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppSyncParameters) -> dict:
    out: dict = {}
    if "graph_ql_operation" in value:
        out["GraphQLOperation"] = value["graph_ql_operation"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AppSyncParameters:
    out: AppSyncParameters = {}  # type: ignore[typeddict-item]
    if "GraphQLOperation" in data:
        out["graph_ql_operation"] = data["GraphQLOperation"]
    return out
