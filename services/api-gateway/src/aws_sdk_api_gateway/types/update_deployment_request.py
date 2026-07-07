"""Generated from Smithy shape ``com.amazonaws.apigateway#UpdateDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_patch_operation
    import aws_sdk_api_gateway.types.string


class UpdateDeploymentRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    deployment_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The replacement identifier for the Deployment resource to change information about.</p>"""
    patch_operations: NotRequired[
        "aws_sdk_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
    ]
    r"""<p>For more information about supported patch operations, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html\">Patch Operations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeploymentRequest) -> dict:
    out: dict = {}
    if "patch_operations" in value:
        import aws_sdk_api_gateway.types.list_of_patch_operation

        out["patchOperations"] = (
            aws_sdk_api_gateway.types.list_of_patch_operation.serialize_json(
                value["patch_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDeploymentRequest:
    out: UpdateDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "patchOperations" in data:
        import aws_sdk_api_gateway.types.list_of_patch_operation

        out["patch_operations"] = (
            aws_sdk_api_gateway.types.list_of_patch_operation.deserialize_json(
                data["patchOperations"]
            )
        )
    return out
