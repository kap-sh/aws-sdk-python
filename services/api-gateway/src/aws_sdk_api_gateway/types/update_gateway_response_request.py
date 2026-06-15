"""Generated from Smithy shape ``com.amazonaws.apigateway#UpdateGatewayResponseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.gateway_response_type
    import aws_sdk_api_gateway.types.list_of_patch_operation
    import aws_sdk_api_gateway.types.string


class UpdateGatewayResponseRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    response_type: "aws_sdk_api_gateway.types.gateway_response_type.GatewayResponseType"
    """<p>The response type of the associated GatewayResponse.</p>"""
    patch_operations: NotRequired[
        "aws_sdk_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
    ]
    r"""<p>For more information about supported patch operations, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html\">Patch Operations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayResponseRequest) -> dict:
    out: dict = {}
    if "patch_operations" in value:
        import aws_sdk_api_gateway.types.list_of_patch_operation

        out["patchOperations"] = (
            aws_sdk_api_gateway.types.list_of_patch_operation.serialize_json(
                value["patch_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGatewayResponseRequest:
    out: UpdateGatewayResponseRequest = {}  # type: ignore[typeddict-item]
    if "patchOperations" in data:
        import aws_sdk_api_gateway.types.list_of_patch_operation

        out["patch_operations"] = (
            aws_sdk_api_gateway.types.list_of_patch_operation.deserialize_json(
                data["patchOperations"]
            )
        )
    return out
