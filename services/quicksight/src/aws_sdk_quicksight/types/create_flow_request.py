"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_id
    import aws_sdk_quicksight.types.create_flow_request_client_token_string
    import aws_sdk_quicksight.types.flow_description_input
    import aws_sdk_quicksight.types.permissions_list
    import aws_sdk_quicksight.types.sensitive_document
    import aws_sdk_quicksight.types.title_input


class CreateFlowRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account where you want to create the flow.</p>"""
    name: "aws_sdk_quicksight.types.title_input.TitleInput"
    """<p>The display name for the flow.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.flow_description_input.FlowDescriptionInput"
    ]
    """<p>The description for the flow.</p>"""
    flow_definition: "aws_sdk_quicksight.types.sensitive_document.SensitiveDocument"
    """<p>The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change.</p> <note> <p>Always derive or depend on the flow definition from the <code>DescribeFlow</code> operation to ensure you are working with the latest format.</p> </note>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.permissions_list.PermissionsList"
    ]
    """<p>Initial permissions for the flow. If omitted, the flow is created without any permissions.</p>"""
    client_token: NotRequired[
        "aws_sdk_quicksight.types.create_flow_request_client_token_string.CreateFlowRequestClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["FlowDefinition"] = value["flow_definition"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.permissions_list

        out["Permissions"] = aws_sdk_quicksight.types.permissions_list.serialize_json(
            value["permissions"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateFlowRequest:
    out: CreateFlowRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateFlowRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "FlowDefinition" in data:
        out["flow_definition"] = data["FlowDefinition"]
    else:
        raise DeserializationError("CreateFlowRequest.flow_definition required")
    if "Permissions" in data:
        import aws_sdk_quicksight.types.permissions_list

        out["permissions"] = aws_sdk_quicksight.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
