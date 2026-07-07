"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_id
    import aws_sdk_quicksight.types.flow_description_input
    import aws_sdk_quicksight.types.flow_id
    import aws_sdk_quicksight.types.sensitive_document
    import aws_sdk_quicksight.types.title_input
    import aws_sdk_quicksight.types.update_flow_request_client_token_string


class UpdateFlowRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that contains the flow that you are updating.</p>"""
    flow_id: "aws_sdk_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow to update.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.title_input.TitleInput"]
    """<p>Updated display name for the flow. Omit to preserve the existing name.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.flow_description_input.FlowDescriptionInput"
    ]
    """<p>Updated description for the flow. Omit to preserve the existing description.</p>"""
    flow_definition: NotRequired[
        "aws_sdk_quicksight.types.sensitive_document.SensitiveDocument"
    ]
    """<p>The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change. When provided, all existing steps are replaced. Omit to preserve the existing definition.</p> <note> <p>Always derive or depend on the flow definition from the <code>DescribeFlow</code> operation to ensure you are working with the latest format.</p> </note>"""
    client_token: NotRequired[
        "aws_sdk_quicksight.types.update_flow_request_client_token_string.UpdateFlowRequestClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "flow_definition" in value:
        out["FlowDefinition"] = value["flow_definition"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateFlowRequest:
    out: UpdateFlowRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "FlowDefinition" in data:
        out["flow_definition"] = data["FlowDefinition"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
