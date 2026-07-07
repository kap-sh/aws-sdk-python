"""Generated from Smithy shape ``com.amazonaws.costexplorer#Anomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly_feedback_type
    import aws_sdk_cost_explorer.types.anomaly_score
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.impact
    import aws_sdk_cost_explorer.types.root_causes
    import aws_sdk_cost_explorer.types.year_month_day


class Anomaly(TypedDict, closed=True):
    anomaly_id: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier for the anomaly. </p>"""
    anomaly_start_date: NotRequired[
        "aws_sdk_cost_explorer.types.year_month_day.YearMonthDay"
    ]
    """<p>The first day the anomaly is detected. </p>"""
    anomaly_end_date: NotRequired[
        "aws_sdk_cost_explorer.types.year_month_day.YearMonthDay"
    ]
    """<p>The last day the anomaly is detected. </p>"""
    dimension_value: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The dimension for the anomaly (for example, an Amazon Web Services service in a service monitor). </p>"""
    root_causes: NotRequired["aws_sdk_cost_explorer.types.root_causes.RootCauses"]
    """<p>The list of identified root causes for the anomaly. </p>"""
    anomaly_score: "aws_sdk_cost_explorer.types.anomaly_score.AnomalyScore"
    """<p>The latest and maximum score for the anomaly. </p>"""
    impact: "aws_sdk_cost_explorer.types.impact.Impact"
    """<p>The dollar impact for the anomaly. </p>"""
    monitor_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) for the cost monitor that generated this anomaly. </p>"""
    feedback: NotRequired[
        "aws_sdk_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType"
    ]
    """<p>The feedback value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Anomaly) -> dict:
    out: dict = {}
    out["AnomalyId"] = value["anomaly_id"]
    if "anomaly_start_date" in value:
        out["AnomalyStartDate"] = value["anomaly_start_date"]
    if "anomaly_end_date" in value:
        out["AnomalyEndDate"] = value["anomaly_end_date"]
    if "dimension_value" in value:
        out["DimensionValue"] = value["dimension_value"]
    if "root_causes" in value:
        import aws_sdk_cost_explorer.types.root_causes

        out["RootCauses"] = (
            aws_sdk_cost_explorer.types.root_causes.serialize_aws_json_1_1(
                value["root_causes"]
            )
        )
    import aws_sdk_cost_explorer.types.anomaly_score

    out["AnomalyScore"] = (
        aws_sdk_cost_explorer.types.anomaly_score.serialize_aws_json_1_1(
            value["anomaly_score"]
        )
    )
    import aws_sdk_cost_explorer.types.impact

    out["Impact"] = aws_sdk_cost_explorer.types.impact.serialize_aws_json_1_1(
        value["impact"]
    )
    out["MonitorArn"] = value["monitor_arn"]
    if "feedback" in value:
        import aws_sdk_cost_explorer.types.anomaly_feedback_type

        out["Feedback"] = (
            aws_sdk_cost_explorer.types.anomaly_feedback_type.serialize_aws_json_1_1(
                value["feedback"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Anomaly:
    out: Anomaly = {}  # type: ignore[typeddict-item]
    if "AnomalyId" in data:
        out["anomaly_id"] = data["AnomalyId"]
    else:
        raise DeserializationError("Anomaly.anomaly_id required")
    if "AnomalyStartDate" in data:
        out["anomaly_start_date"] = data["AnomalyStartDate"]
    if "AnomalyEndDate" in data:
        out["anomaly_end_date"] = data["AnomalyEndDate"]
    if "DimensionValue" in data:
        out["dimension_value"] = data["DimensionValue"]
    if "RootCauses" in data:
        import aws_sdk_cost_explorer.types.root_causes

        out["root_causes"] = (
            aws_sdk_cost_explorer.types.root_causes.deserialize_aws_json_1_1(
                data["RootCauses"]
            )
        )
    if "AnomalyScore" in data:
        import aws_sdk_cost_explorer.types.anomaly_score

        out["anomaly_score"] = (
            aws_sdk_cost_explorer.types.anomaly_score.deserialize_aws_json_1_1(
                data["AnomalyScore"]
            )
        )
    else:
        raise DeserializationError("Anomaly.anomaly_score required")
    if "Impact" in data:
        import aws_sdk_cost_explorer.types.impact

        out["impact"] = aws_sdk_cost_explorer.types.impact.deserialize_aws_json_1_1(
            data["Impact"]
        )
    else:
        raise DeserializationError("Anomaly.impact required")
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("Anomaly.monitor_arn required")
    if "Feedback" in data:
        import aws_sdk_cost_explorer.types.anomaly_feedback_type

        out["feedback"] = (
            aws_sdk_cost_explorer.types.anomaly_feedback_type.deserialize_aws_json_1_1(
                data["Feedback"]
            )
        )
    return out
