"""Generated from Smithy shape ``com.amazonaws.xray#InsightImpactGraphService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_impact_graph_edge_list
    import aws_sdk_xray.types.nullable_integer
    import aws_sdk_xray.types.service_names
    import aws_sdk_xray.types.string


class InsightImpactGraphService(TypedDict, closed=True):
    reference_id: NotRequired["aws_sdk_xray.types.nullable_integer.NullableInteger"]
    """<p>Identifier for the service. Unique within the service map.</p>"""
    type: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Identifier for the service. Unique within the service map.</p> <ul> <li> <p>Amazon Web Services Resource - The type of an Amazon Web Services resource. For example, AWS::EC2::Instance for an application running on Amazon EC2 or AWS::DynamoDB::Table for an Amazon DynamoDB table that the application used. </p> </li> <li> <p>Amazon Web Services Service - The type of an Amazon Web Services service. For example, AWS::DynamoDB for downstream calls to Amazon DynamoDB that didn't target a specific table. </p> </li> <li> <p>Amazon Web Services Service - The type of an Amazon Web Services service. For example, AWS::DynamoDB for downstream calls to Amazon DynamoDB that didn't target a specific table. </p> </li> <li> <p>remote - A downstream service of indeterminate type.</p> </li> </ul>"""
    name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The canonical name of the service.</p>"""
    names: NotRequired["aws_sdk_xray.types.service_names.ServiceNames"]
    """<p>A list of names for the service, including the canonical name.</p>"""
    account_id: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Identifier of the Amazon Web Services account in which the service runs.</p>"""
    edges: NotRequired[
        "aws_sdk_xray.types.insight_impact_graph_edge_list.InsightImpactGraphEdgeList"
    ]
    """<p>Connections to downstream services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightImpactGraphService) -> dict:
    out: dict = {}
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "names" in value:
        import aws_sdk_xray.types.service_names

        out["Names"] = aws_sdk_xray.types.service_names.serialize_json(value["names"])
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "edges" in value:
        import aws_sdk_xray.types.insight_impact_graph_edge_list

        out["Edges"] = aws_sdk_xray.types.insight_impact_graph_edge_list.serialize_json(
            value["edges"]
        )
    return out


def deserialize_json(data: dict) -> InsightImpactGraphService:
    out: InsightImpactGraphService = {}  # type: ignore[typeddict-item]
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Names" in data:
        import aws_sdk_xray.types.service_names

        out["names"] = aws_sdk_xray.types.service_names.deserialize_json(data["Names"])
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Edges" in data:
        import aws_sdk_xray.types.insight_impact_graph_edge_list

        out["edges"] = (
            aws_sdk_xray.types.insight_impact_graph_edge_list.deserialize_json(
                data["Edges"]
            )
        )
    return out
