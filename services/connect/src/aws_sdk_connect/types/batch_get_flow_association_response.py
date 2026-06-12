"""Generated from Smithy shape ``com.amazonaws.connect#BatchGetFlowAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.flow_association_summary_list


class BatchGetFlowAssociationResponse(TypedDict):
    flow_association_summary_list: NotRequired[
        "aws_sdk_connect.types.flow_association_summary_list.FlowAssociationSummaryList"
    ]
    """<p>Information about flow associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFlowAssociationResponse) -> dict:
    out: dict = {}
    if "flow_association_summary_list" in value:
        import aws_sdk_connect.types.flow_association_summary_list

        out["FlowAssociationSummaryList"] = (
            aws_sdk_connect.types.flow_association_summary_list.serialize_json(
                value["flow_association_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetFlowAssociationResponse:
    out: BatchGetFlowAssociationResponse = {}  # type: ignore[typeddict-item]
    if "FlowAssociationSummaryList" in data:
        import aws_sdk_connect.types.flow_association_summary_list

        out["flow_association_summary_list"] = (
            aws_sdk_connect.types.flow_association_summary_list.deserialize_json(
                data["FlowAssociationSummaryList"]
            )
        )
    return out
