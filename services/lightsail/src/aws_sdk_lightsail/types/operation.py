"""Generated from Smithy shape ``com.amazonaws.lightsail#Operation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.operation_status
    import aws_sdk_lightsail.types.operation_type
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string


class Operation(TypedDict):
    id: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the operation.</p>"""
    resource_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The resource name.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The resource type. </p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the operation was initialized (<code>1479816991.349</code>).</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>The Amazon Web Services Region and Availability Zone.</p>"""
    is_terminal: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the operation is terminal.</p>"""
    operation_details: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Details about the operation (<code>Debian-1GB-Ohio-1</code>).</p>"""
    operation_type: NotRequired["aws_sdk_lightsail.types.operation_type.OperationType"]
    """<p>The type of operation. </p>"""
    status: NotRequired["aws_sdk_lightsail.types.operation_status.OperationStatus"]
    """<p>The status of the operation. </p>"""
    status_changed_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the status was changed (<code>1479816991.349</code>).</p>"""
    error_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The error code.</p>"""
    error_details: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The error details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operation) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "is_terminal" in value:
        out["isTerminal"] = value["is_terminal"]
    if "operation_details" in value:
        out["operationDetails"] = value["operation_details"]
    if "operation_type" in value:
        import aws_sdk_lightsail.types.operation_type

        out["operationType"] = (
            aws_sdk_lightsail.types.operation_type.serialize_aws_json_1_1(
                value["operation_type"]
            )
        )
    if "status" in value:
        import aws_sdk_lightsail.types.operation_status

        out["status"] = aws_sdk_lightsail.types.operation_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_changed_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["statusChangedAt"] = (
            aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
                value["status_changed_at"]
            )
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_details" in value:
        out["errorDetails"] = value["error_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "isTerminal" in data:
        out["is_terminal"] = data["isTerminal"]
    if "operationDetails" in data:
        out["operation_details"] = data["operationDetails"]
    if "operationType" in data:
        import aws_sdk_lightsail.types.operation_type

        out["operation_type"] = (
            aws_sdk_lightsail.types.operation_type.deserialize_aws_json_1_1(
                data["operationType"]
            )
        )
    if "status" in data:
        import aws_sdk_lightsail.types.operation_status

        out["status"] = (
            aws_sdk_lightsail.types.operation_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusChangedAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["status_changed_at"] = (
            aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
                data["statusChangedAt"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorDetails" in data:
        out["error_details"] = data["errorDetails"]
    return out
