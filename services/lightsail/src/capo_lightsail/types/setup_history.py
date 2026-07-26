"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.setup_execution_details_list
    import capo_lightsail.types.setup_history_resource
    import capo_lightsail.types.setup_request
    import capo_lightsail.types.setup_status


class SetupHistory(TypedDict, closed=True):
    operation_id: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>A GUID that's used to identify the operation.</p>"""
    request: NotRequired["capo_lightsail.types.setup_request.SetupRequest"]
    """<p>Information about the specified request.</p>"""
    resource: NotRequired[
        "capo_lightsail.types.setup_history_resource.SetupHistoryResource"
    ]
    """<p>The target resource name for the request.</p>"""
    execution_details: NotRequired[
        "capo_lightsail.types.setup_execution_details_list.SetupExecutionDetailsList"
    ]
    """<p>Describes the full details of the request.</p>"""
    status: NotRequired["capo_lightsail.types.setup_status.SetupStatus"]
    """<p>The status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupHistory) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["operationId"] = value["operation_id"]
    if "request" in value:
        import capo_lightsail.types.setup_request

        out["request"] = capo_lightsail.types.setup_request.serialize_aws_json_1_1(
            value["request"]
        )
    if "resource" in value:
        import capo_lightsail.types.setup_history_resource

        out["resource"] = (
            capo_lightsail.types.setup_history_resource.serialize_aws_json_1_1(
                value["resource"]
            )
        )
    if "execution_details" in value:
        import capo_lightsail.types.setup_execution_details_list

        out["executionDetails"] = (
            capo_lightsail.types.setup_execution_details_list.serialize_aws_json_1_1(
                value["execution_details"]
            )
        )
    if "status" in value:
        import capo_lightsail.types.setup_status

        out["status"] = capo_lightsail.types.setup_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetupHistory:
    out: SetupHistory = {}  # type: ignore[typeddict-item]
    if "operationId" in data:
        out["operation_id"] = data["operationId"]
    if "request" in data:
        import capo_lightsail.types.setup_request

        out["request"] = capo_lightsail.types.setup_request.deserialize_aws_json_1_1(
            data["request"]
        )
    if "resource" in data:
        import capo_lightsail.types.setup_history_resource

        out["resource"] = (
            capo_lightsail.types.setup_history_resource.deserialize_aws_json_1_1(
                data["resource"]
            )
        )
    if "executionDetails" in data:
        import capo_lightsail.types.setup_execution_details_list

        out["execution_details"] = (
            capo_lightsail.types.setup_execution_details_list.deserialize_aws_json_1_1(
                data["executionDetails"]
            )
        )
    if "status" in data:
        import capo_lightsail.types.setup_status

        out["status"] = capo_lightsail.types.setup_status.deserialize_aws_json_1_1(
            data["status"]
        )
    return out
