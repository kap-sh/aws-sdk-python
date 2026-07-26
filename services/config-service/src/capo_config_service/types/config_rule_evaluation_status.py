"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleEvaluationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.boolean
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.date
    import capo_config_service.types.string


class ConfigRuleEvaluationStatus(TypedDict, closed=True):
    config_rule_name: NotRequired[
        "capo_config_service.types.config_rule_name.ConfigRuleName"
    ]
    """<p>The name of the Config rule.</p>"""
    config_rule_arn: NotRequired["capo_config_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Config rule.</p>"""
    config_rule_id: NotRequired["capo_config_service.types.string.String"]
    """<p>The ID of the Config rule.</p>"""
    last_successful_invocation_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time that Config last successfully invoked the Config rule to evaluate your Amazon Web Services resources.</p>"""
    last_failed_invocation_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time that Config last failed to invoke the Config rule to evaluate your Amazon Web Services resources.</p>"""
    last_successful_evaluation_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time that Config last successfully evaluated your Amazon Web Services resources against the rule.</p>"""
    last_failed_evaluation_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time that Config last failed to evaluate your Amazon Web Services resources against the rule.</p>"""
    first_activated_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time that you first activated the Config rule.</p>"""
    last_deactivated_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time that you last turned off the Config rule.</p>"""
    last_error_code: NotRequired["capo_config_service.types.string.String"]
    """<p>The error code that Config returned when the rule last failed.</p>"""
    last_error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>The error message that Config returned when the rule last failed.</p>"""
    first_evaluation_started: "capo_config_service.types.boolean.Boolean"
    """<p>Indicates whether Config has evaluated your resources against the rule at least once.</p> <ul> <li> <p> <code>true</code> - Config has evaluated your Amazon Web Services resources against the rule at least once.</p> </li> <li> <p> <code>false</code> - Config has not finished evaluating your Amazon Web Services resources against the rule at least once.</p> </li> </ul>"""
    last_debug_log_delivery_status: NotRequired[
        "capo_config_service.types.string.String"
    ]
    """<p>The status of the last attempted delivery of a debug log for your Config Custom Policy rules. Either <code>Successful</code> or <code>Failed</code>.</p>"""
    last_debug_log_delivery_status_reason: NotRequired[
        "capo_config_service.types.string.String"
    ]
    """<p>The reason Config was not able to deliver a debug log. This is for the last failed attempt to retrieve a debug log for your Config Custom Policy rules.</p>"""
    last_debug_log_delivery_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time Config last attempted to deliver a debug log for your Config Custom Policy rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRuleEvaluationStatus) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    if "config_rule_arn" in value:
        out["ConfigRuleArn"] = value["config_rule_arn"]
    if "config_rule_id" in value:
        out["ConfigRuleId"] = value["config_rule_id"]
    if "last_successful_invocation_time" in value:
        import capo_config_service.types.date

        out["LastSuccessfulInvocationTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_successful_invocation_time"]
            )
        )
    if "last_failed_invocation_time" in value:
        import capo_config_service.types.date

        out["LastFailedInvocationTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_failed_invocation_time"]
            )
        )
    if "last_successful_evaluation_time" in value:
        import capo_config_service.types.date

        out["LastSuccessfulEvaluationTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_successful_evaluation_time"]
            )
        )
    if "last_failed_evaluation_time" in value:
        import capo_config_service.types.date

        out["LastFailedEvaluationTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_failed_evaluation_time"]
            )
        )
    if "first_activated_time" in value:
        import capo_config_service.types.date

        out["FirstActivatedTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["first_activated_time"]
            )
        )
    if "last_deactivated_time" in value:
        import capo_config_service.types.date

        out["LastDeactivatedTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_deactivated_time"]
            )
        )
    if "last_error_code" in value:
        out["LastErrorCode"] = value["last_error_code"]
    if "last_error_message" in value:
        out["LastErrorMessage"] = value["last_error_message"]
    out["FirstEvaluationStarted"] = value.get("first_evaluation_started", False)
    if "last_debug_log_delivery_status" in value:
        out["LastDebugLogDeliveryStatus"] = value["last_debug_log_delivery_status"]
    if "last_debug_log_delivery_status_reason" in value:
        out["LastDebugLogDeliveryStatusReason"] = value[
            "last_debug_log_delivery_status_reason"
        ]
    if "last_debug_log_delivery_time" in value:
        import capo_config_service.types.date

        out["LastDebugLogDeliveryTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_debug_log_delivery_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigRuleEvaluationStatus:
    out: ConfigRuleEvaluationStatus = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    if "ConfigRuleArn" in data:
        out["config_rule_arn"] = data["ConfigRuleArn"]
    if "ConfigRuleId" in data:
        out["config_rule_id"] = data["ConfigRuleId"]
    if "LastSuccessfulInvocationTime" in data:
        import capo_config_service.types.date

        out["last_successful_invocation_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastSuccessfulInvocationTime"]
            )
        )
    if "LastFailedInvocationTime" in data:
        import capo_config_service.types.date

        out["last_failed_invocation_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastFailedInvocationTime"]
            )
        )
    if "LastSuccessfulEvaluationTime" in data:
        import capo_config_service.types.date

        out["last_successful_evaluation_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastSuccessfulEvaluationTime"]
            )
        )
    if "LastFailedEvaluationTime" in data:
        import capo_config_service.types.date

        out["last_failed_evaluation_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastFailedEvaluationTime"]
            )
        )
    if "FirstActivatedTime" in data:
        import capo_config_service.types.date

        out["first_activated_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["FirstActivatedTime"]
            )
        )
    if "LastDeactivatedTime" in data:
        import capo_config_service.types.date

        out["last_deactivated_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastDeactivatedTime"]
            )
        )
    if "LastErrorCode" in data:
        out["last_error_code"] = data["LastErrorCode"]
    if "LastErrorMessage" in data:
        out["last_error_message"] = data["LastErrorMessage"]
    if "FirstEvaluationStarted" in data:
        out["first_evaluation_started"] = data["FirstEvaluationStarted"]
    else:
        out["first_evaluation_started"] = False
    if "LastDebugLogDeliveryStatus" in data:
        out["last_debug_log_delivery_status"] = data["LastDebugLogDeliveryStatus"]
    if "LastDebugLogDeliveryStatusReason" in data:
        out["last_debug_log_delivery_status_reason"] = data[
            "LastDebugLogDeliveryStatusReason"
        ]
    if "LastDebugLogDeliveryTime" in data:
        import capo_config_service.types.date

        out["last_debug_log_delivery_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastDebugLogDeliveryTime"]
            )
        )
    return out
