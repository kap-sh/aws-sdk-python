"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppFlowOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_application_info
    import aws_sdk_socialmessaging.types.meta_flow_category_list
    import aws_sdk_socialmessaging.types.meta_flow_data_api_version
    import aws_sdk_socialmessaging.types.meta_flow_endpoint_uri
    import aws_sdk_socialmessaging.types.meta_flow_health_status
    import aws_sdk_socialmessaging.types.meta_flow_id
    import aws_sdk_socialmessaging.types.meta_flow_json_version
    import aws_sdk_socialmessaging.types.meta_flow_name
    import aws_sdk_socialmessaging.types.meta_flow_preview_info
    import aws_sdk_socialmessaging.types.meta_flow_status
    import aws_sdk_socialmessaging.types.meta_flow_whats_app_business_account_info
    import aws_sdk_socialmessaging.types.validation_error_list


class GetWhatsAppFlowOutput(TypedDict, closed=True):
    flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow.</p>"""
    flow_name: "aws_sdk_socialmessaging.types.meta_flow_name.MetaFlowName"
    """<p>The name of the Flow.</p>"""
    flow_status: "aws_sdk_socialmessaging.types.meta_flow_status.MetaFlowStatus"
    """<p>The lifecycle status of the Flow. Valid values are DRAFT, PUBLISHED, DEPRECATED, BLOCKED, and THROTTLED.</p>"""
    categories: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
    ]
    """<p>The categories that classify the business purpose of the Flow.</p>"""
    validation_errors: NotRequired[
        "aws_sdk_socialmessaging.types.validation_error_list.ValidationErrorList"
    ]
    """<p>A list of validation errors from Meta, if any.</p>"""
    json_version: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_json_version.MetaFlowJsonVersion"
    ]
    """<p>The version of the Flow JSON schema used by this Flow (for example, 7.3).</p>"""
    data_api_version: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_data_api_version.MetaFlowDataApiVersion"
    ]
    """<p>The data API version for data exchange endpoint Flows.</p>"""
    endpoint_uri: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_endpoint_uri.MetaFlowEndpointUri"
    ]
    """<p>The endpoint URI for data exchange Flows, if configured.</p>"""
    preview: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_preview_info.MetaFlowPreviewInfo"
    ]
    """<p>The preview URL and its expiration timestamp for testing the Flow.</p>"""
    whats_app_business_account: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_whats_app_business_account_info.MetaFlowWhatsAppBusinessAccountInfo"
    ]
    """<p>The WhatsApp Business Account information from Meta associated with this Flow.</p>"""
    application: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_application_info.MetaFlowApplicationInfo"
    ]
    """<p>The Meta application information associated with this Flow.</p>"""
    health_status: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_health_status.MetaFlowHealthStatus"
    ]
    """<p>The health status information for this Flow from Meta.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppFlowOutput) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    out["flowName"] = value["flow_name"]
    out["flowStatus"] = value["flow_status"]
    if "categories" in value:
        import aws_sdk_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            aws_sdk_socialmessaging.types.meta_flow_category_list.serialize_json(
                value["categories"]
            )
        )
    if "validation_errors" in value:
        import aws_sdk_socialmessaging.types.validation_error_list

        out["validationErrors"] = (
            aws_sdk_socialmessaging.types.validation_error_list.serialize_json(
                value["validation_errors"]
            )
        )
    if "json_version" in value:
        out["jsonVersion"] = value["json_version"]
    if "data_api_version" in value:
        out["dataApiVersion"] = value["data_api_version"]
    if "endpoint_uri" in value:
        out["endpointUri"] = value["endpoint_uri"]
    if "preview" in value:
        import aws_sdk_socialmessaging.types.meta_flow_preview_info

        out["preview"] = (
            aws_sdk_socialmessaging.types.meta_flow_preview_info.serialize_json(
                value["preview"]
            )
        )
    if "whats_app_business_account" in value:
        import aws_sdk_socialmessaging.types.meta_flow_whats_app_business_account_info

        out["whatsAppBusinessAccount"] = (
            aws_sdk_socialmessaging.types.meta_flow_whats_app_business_account_info.serialize_json(
                value["whats_app_business_account"]
            )
        )
    if "application" in value:
        import aws_sdk_socialmessaging.types.meta_flow_application_info

        out["application"] = (
            aws_sdk_socialmessaging.types.meta_flow_application_info.serialize_json(
                value["application"]
            )
        )
    if "health_status" in value:
        import aws_sdk_socialmessaging.types.meta_flow_health_status

        out["healthStatus"] = (
            aws_sdk_socialmessaging.types.meta_flow_health_status.serialize_json(
                value["health_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWhatsAppFlowOutput:
    out: GetWhatsAppFlowOutput = {}  # type: ignore[typeddict-item]
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("GetWhatsAppFlowOutput.flow_id required")
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError("GetWhatsAppFlowOutput.flow_name required")
    if "flowStatus" in data:
        out["flow_status"] = data["flowStatus"]
    else:
        raise DeserializationError("GetWhatsAppFlowOutput.flow_status required")
    if "categories" in data:
        import aws_sdk_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            aws_sdk_socialmessaging.types.meta_flow_category_list.deserialize_json(
                data["categories"]
            )
        )
    if "validationErrors" in data:
        import aws_sdk_socialmessaging.types.validation_error_list

        out["validation_errors"] = (
            aws_sdk_socialmessaging.types.validation_error_list.deserialize_json(
                data["validationErrors"]
            )
        )
    if "jsonVersion" in data:
        out["json_version"] = data["jsonVersion"]
    if "dataApiVersion" in data:
        out["data_api_version"] = data["dataApiVersion"]
    if "endpointUri" in data:
        out["endpoint_uri"] = data["endpointUri"]
    if "preview" in data:
        import aws_sdk_socialmessaging.types.meta_flow_preview_info

        out["preview"] = (
            aws_sdk_socialmessaging.types.meta_flow_preview_info.deserialize_json(
                data["preview"]
            )
        )
    if "whatsAppBusinessAccount" in data:
        import aws_sdk_socialmessaging.types.meta_flow_whats_app_business_account_info

        out["whats_app_business_account"] = (
            aws_sdk_socialmessaging.types.meta_flow_whats_app_business_account_info.deserialize_json(
                data["whatsAppBusinessAccount"]
            )
        )
    if "application" in data:
        import aws_sdk_socialmessaging.types.meta_flow_application_info

        out["application"] = (
            aws_sdk_socialmessaging.types.meta_flow_application_info.deserialize_json(
                data["application"]
            )
        )
    if "healthStatus" in data:
        import aws_sdk_socialmessaging.types.meta_flow_health_status

        out["health_status"] = (
            aws_sdk_socialmessaging.types.meta_flow_health_status.deserialize_json(
                data["healthStatus"]
            )
        )
    return out
