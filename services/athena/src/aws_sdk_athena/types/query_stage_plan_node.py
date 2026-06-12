"""Generated from Smithy shape ``com.amazonaws.athena#QueryStagePlanNode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_stage_plan_nodes
    import aws_sdk_athena.types.string
    import aws_sdk_athena.types.string_list


class QueryStagePlanNode(TypedDict):
    name: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>Name of the query stage plan that describes the operation this stage is performing as part of query execution.</p>"""
    identifier: NotRequired["aws_sdk_athena.types.string.String"]
    """<p>Information about the operation this query stage plan node is performing.</p>"""
    children: NotRequired[
        "aws_sdk_athena.types.query_stage_plan_nodes.QueryStagePlanNodes"
    ]
    """<p>Stage plan information such as name, identifier, sub plans, and remote sources of child plan nodes/</p>"""
    remote_sources: NotRequired["aws_sdk_athena.types.string_list.StringList"]
    """<p>Source plan node IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStagePlanNode) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "children" in value:
        import aws_sdk_athena.types.query_stage_plan_nodes

        out["Children"] = (
            aws_sdk_athena.types.query_stage_plan_nodes.serialize_aws_json_1_1(
                value["children"]
            )
        )
    if "remote_sources" in value:
        import aws_sdk_athena.types.string_list

        out["RemoteSources"] = aws_sdk_athena.types.string_list.serialize_aws_json_1_1(
            value["remote_sources"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStagePlanNode:
    out: QueryStagePlanNode = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "Children" in data:
        import aws_sdk_athena.types.query_stage_plan_nodes

        out["children"] = (
            aws_sdk_athena.types.query_stage_plan_nodes.deserialize_aws_json_1_1(
                data["Children"]
            )
        )
    if "RemoteSources" in data:
        import aws_sdk_athena.types.string_list

        out["remote_sources"] = (
            aws_sdk_athena.types.string_list.deserialize_aws_json_1_1(
                data["RemoteSources"]
            )
        )
    return out
