"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppVersionResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.aws_region
    import aws_sdk_resiliencehub.types.client_token
    import aws_sdk_resiliencehub.types.customer_id
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.logical_resource_id
    import aws_sdk_resiliencehub.types.string2048


class DeleteAppVersionResourceRequest(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    resource_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the resource.</p>"""
    logical_resource_id: NotRequired[
        "aws_sdk_resiliencehub.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>Logical identifier of the resource.</p>"""
    physical_resource_id: NotRequired[
        "aws_sdk_resiliencehub.types.string2048.String2048"
    ]
    """<p>Physical identifier of the resource.</p>"""
    aws_region: NotRequired["aws_sdk_resiliencehub.types.aws_region.AwsRegion"]
    """<p>Amazon Web Services region that owns the physical resource.</p>"""
    aws_account_id: NotRequired["aws_sdk_resiliencehub.types.customer_id.CustomerId"]
    """<p>Amazon Web Services account that owns the physical resource.</p>"""
    client_token: NotRequired["aws_sdk_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppVersionResourceRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "logical_resource_id" in value:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logicalResourceId"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.serialize_json(
                value["logical_resource_id"]
            )
        )
    if "physical_resource_id" in value:
        out["physicalResourceId"] = value["physical_resource_id"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteAppVersionResourceRequest:
    out: DeleteAppVersionResourceRequest = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("DeleteAppVersionResourceRequest.app_arn required")
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "logicalResourceId" in data:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    if "physicalResourceId" in data:
        out["physical_resource_id"] = data["physicalResourceId"]
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
