"""Generated from Smithy shape ``com.amazonaws.apigateway#UpdateDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_patch_operation
    import aws_sdk_api_gateway.types.string


class UpdateDomainNameRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the DomainName resource to be changed.</p>"""
    domain_name_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p> The identifier for the domain name resource. Supported only for private custom domain names. </p>"""
    patch_operations: NotRequired[
        "aws_sdk_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
    ]
    r"""<p>For more information about supported patch operations, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html\">Patch Operations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainNameRequest) -> dict:
    out: dict = {}
    if "patch_operations" in value:
        import aws_sdk_api_gateway.types.list_of_patch_operation

        out["patchOperations"] = (
            aws_sdk_api_gateway.types.list_of_patch_operation.serialize_json(
                value["patch_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDomainNameRequest:
    out: UpdateDomainNameRequest = {}  # type: ignore[typeddict-item]
    if "patchOperations" in data:
        import aws_sdk_api_gateway.types.list_of_patch_operation

        out["patch_operations"] = (
            aws_sdk_api_gateway.types.list_of_patch_operation.deserialize_json(
                data["patchOperations"]
            )
        )
    return out
