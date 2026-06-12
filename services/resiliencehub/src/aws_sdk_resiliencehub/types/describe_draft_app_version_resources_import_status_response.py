"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeDraftAppVersionResourcesImportStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.error_detail_list
    import aws_sdk_resiliencehub.types.resource_import_status_type
    import aws_sdk_resiliencehub.types.string500
    import aws_sdk_resiliencehub.types.time_stamp


class DescribeDraftAppVersionResourcesImportStatusResponse(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    """<p>The version of the application.</p>"""
    status: "aws_sdk_resiliencehub.types.resource_import_status_type.ResourceImportStatusType"
    """<p>Status of the action.</p>"""
    status_change_time: "aws_sdk_resiliencehub.types.time_stamp.TimeStamp"
    """<p>The time when the status last changed.</p>"""
    error_message: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>The error message returned for the resource request.</p>"""
    error_details: NotRequired[
        "aws_sdk_resiliencehub.types.error_detail_list.ErrorDetailList"
    ]
    """<p>List of errors that were encountered while importing resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDraftAppVersionResourcesImportStatusResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    import aws_sdk_resiliencehub.types.resource_import_status_type

    out["status"] = (
        aws_sdk_resiliencehub.types.resource_import_status_type.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_resiliencehub.types.time_stamp

    out["statusChangeTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
        value["status_change_time"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_details" in value:
        import aws_sdk_resiliencehub.types.error_detail_list

        out["errorDetails"] = (
            aws_sdk_resiliencehub.types.error_detail_list.serialize_json(
                value["error_details"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> DescribeDraftAppVersionResourcesImportStatusResponse:
    out: DescribeDraftAppVersionResourcesImportStatusResponse = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.app_arn required"
        )
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.app_version required"
        )
    if "status" in data:
        import aws_sdk_resiliencehub.types.resource_import_status_type

        out["status"] = (
            aws_sdk_resiliencehub.types.resource_import_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.status required"
        )
    if "statusChangeTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["status_change_time"] = (
            aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
                data["statusChangeTime"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.status_change_time required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorDetails" in data:
        import aws_sdk_resiliencehub.types.error_detail_list

        out["error_details"] = (
            aws_sdk_resiliencehub.types.error_detail_list.deserialize_json(
                data["errorDetails"]
            )
        )
    return out
