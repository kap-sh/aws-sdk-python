"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackStatusDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_arn
    import aws_sdk_config_service.types.conformance_pack_id
    import aws_sdk_config_service.types.conformance_pack_name
    import aws_sdk_config_service.types.conformance_pack_state
    import aws_sdk_config_service.types.conformance_pack_status_reason
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.stack_arn


class ConformancePackStatusDetail(TypedDict):
    conformance_pack_name: (
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    conformance_pack_id: (
        "aws_sdk_config_service.types.conformance_pack_id.ConformancePackId"
    )
    """<p>ID of the conformance pack.</p>"""
    conformance_pack_arn: (
        "aws_sdk_config_service.types.conformance_pack_arn.ConformancePackArn"
    )
    """<p>Amazon Resource Name (ARN) of comformance pack.</p>"""
    conformance_pack_state: (
        "aws_sdk_config_service.types.conformance_pack_state.ConformancePackState"
    )
    """<p>Indicates deployment status of conformance pack.</p> <p>Config sets the state of the conformance pack to:</p> <ul> <li> <p>CREATE_IN_PROGRESS when a conformance pack creation is in progress for an account.</p> </li> <li> <p>CREATE_COMPLETE when a conformance pack has been successfully created in your account.</p> </li> <li> <p>CREATE_FAILED when a conformance pack creation failed in your account.</p> </li> <li> <p>DELETE_IN_PROGRESS when a conformance pack deletion is in progress. </p> </li> <li> <p>DELETE_FAILED when a conformance pack deletion failed in your account.</p> </li> </ul>"""
    stack_arn: "aws_sdk_config_service.types.stack_arn.StackArn"
    """<p>Amazon Resource Name (ARN) of CloudFormation stack. </p>"""
    conformance_pack_status_reason: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_status_reason.ConformancePackStatusReason"
    ]
    """<p>The reason of conformance pack creation failure.</p>"""
    last_update_requested_time: "aws_sdk_config_service.types.date.Date"
    """<p>Last time when conformation pack creation and update was requested.</p>"""
    last_update_completed_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>Last time when conformation pack creation and update was successful.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackStatusDetail) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    out["ConformancePackId"] = value["conformance_pack_id"]
    out["ConformancePackArn"] = value["conformance_pack_arn"]
    import aws_sdk_config_service.types.conformance_pack_state

    out["ConformancePackState"] = (
        aws_sdk_config_service.types.conformance_pack_state.serialize_aws_json_1_1(
            value["conformance_pack_state"]
        )
    )
    out["StackArn"] = value["stack_arn"]
    if "conformance_pack_status_reason" in value:
        out["ConformancePackStatusReason"] = value["conformance_pack_status_reason"]
    import aws_sdk_config_service.types.date

    out["LastUpdateRequestedTime"] = (
        aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["last_update_requested_time"]
        )
    )
    if "last_update_completed_time" in value:
        import aws_sdk_config_service.types.date

        out["LastUpdateCompletedTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_update_completed_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackStatusDetail:
    out: ConformancePackStatusDetail = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "ConformancePackStatusDetail.conformance_pack_name required"
        )
    if "ConformancePackId" in data:
        out["conformance_pack_id"] = data["ConformancePackId"]
    else:
        raise DeserializationError(
            "ConformancePackStatusDetail.conformance_pack_id required"
        )
    if "ConformancePackArn" in data:
        out["conformance_pack_arn"] = data["ConformancePackArn"]
    else:
        raise DeserializationError(
            "ConformancePackStatusDetail.conformance_pack_arn required"
        )
    if "ConformancePackState" in data:
        import aws_sdk_config_service.types.conformance_pack_state

        out["conformance_pack_state"] = (
            aws_sdk_config_service.types.conformance_pack_state.deserialize_aws_json_1_1(
                data["ConformancePackState"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackStatusDetail.conformance_pack_state required"
        )
    if "StackArn" in data:
        out["stack_arn"] = data["StackArn"]
    else:
        raise DeserializationError("ConformancePackStatusDetail.stack_arn required")
    if "ConformancePackStatusReason" in data:
        out["conformance_pack_status_reason"] = data["ConformancePackStatusReason"]
    if "LastUpdateRequestedTime" in data:
        import aws_sdk_config_service.types.date

        out["last_update_requested_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateRequestedTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackStatusDetail.last_update_requested_time required"
        )
    if "LastUpdateCompletedTime" in data:
        import aws_sdk_config_service.types.date

        out["last_update_completed_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateCompletedTime"]
            )
        )
    return out
