"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppVersionResourcesResolutionStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.resource_resolution_status_type
    import aws_sdk_resiliencehub.types.string255
    import aws_sdk_resiliencehub.types.string500


class DescribeAppVersionResourcesResolutionStatusResponse(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    """<p>The version of the application.</p>"""
    resolution_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>The identifier for a specific resolution.</p>"""
    status: "aws_sdk_resiliencehub.types.resource_resolution_status_type.ResourceResolutionStatusType"
    """<p>Status of the action.</p>"""
    error_message: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>The returned error message for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppVersionResourcesResolutionStatusResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    out["resolutionId"] = value["resolution_id"]
    import aws_sdk_resiliencehub.types.resource_resolution_status_type

    out["status"] = (
        aws_sdk_resiliencehub.types.resource_resolution_status_type.serialize_json(
            value["status"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> DescribeAppVersionResourcesResolutionStatusResponse:
    out: DescribeAppVersionResourcesResolutionStatusResponse = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DescribeAppVersionResourcesResolutionStatusResponse.app_arn required"
        )
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "DescribeAppVersionResourcesResolutionStatusResponse.app_version required"
        )
    if "resolutionId" in data:
        out["resolution_id"] = data["resolutionId"]
    else:
        raise DeserializationError(
            "DescribeAppVersionResourcesResolutionStatusResponse.resolution_id required"
        )
    if "status" in data:
        import aws_sdk_resiliencehub.types.resource_resolution_status_type

        out["status"] = (
            aws_sdk_resiliencehub.types.resource_resolution_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAppVersionResourcesResolutionStatusResponse.status required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
