"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_state_list
    import aws_sdk_inspector.types.duration_range
    import aws_sdk_inspector.types.filter_rules_package_arn_list
    import aws_sdk_inspector.types.name_pattern
    import aws_sdk_inspector.types.timestamp_range


class AssessmentRunFilter(TypedDict):
    name_pattern: NotRequired["aws_sdk_inspector.types.name_pattern.NamePattern"]
    """<p>For a record to match a filter, an explicit value or a string containing a wildcard that is specified for this data type property must match the value of the <b>assessmentRunName</b> property of the <a>AssessmentRun</a> data type.</p>"""
    states: NotRequired[
        "aws_sdk_inspector.types.assessment_run_state_list.AssessmentRunStateList"
    ]
    """<p>For a record to match a filter, one of the values specified for this data type property must be the exact match of the value of the <b>assessmentRunState</b> property of the <a>AssessmentRun</a> data type.</p>"""
    duration_range: NotRequired["aws_sdk_inspector.types.duration_range.DurationRange"]
    """<p>For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the <b>durationInSeconds</b> property of the <a>AssessmentRun</a> data type.</p>"""
    rules_package_arns: NotRequired[
        "aws_sdk_inspector.types.filter_rules_package_arn_list.FilterRulesPackageArnList"
    ]
    """<p>For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the <b>rulesPackages</b> property of the <a>AssessmentRun</a> data type.</p>"""
    start_time_range: NotRequired[
        "aws_sdk_inspector.types.timestamp_range.TimestampRange"
    ]
    """<p>For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the <b>startTime</b> property of the <a>AssessmentRun</a> data type.</p>"""
    completion_time_range: NotRequired[
        "aws_sdk_inspector.types.timestamp_range.TimestampRange"
    ]
    """<p>For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the <b>completedAt</b> property of the <a>AssessmentRun</a> data type.</p>"""
    state_change_time_range: NotRequired[
        "aws_sdk_inspector.types.timestamp_range.TimestampRange"
    ]
    """<p>For a record to match a filter, the value that is specified for this data type property must match the <b>stateChangedAt</b> property of the <a>AssessmentRun</a> data type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunFilter) -> dict:
    out: dict = {}
    if "name_pattern" in value:
        out["namePattern"] = value["name_pattern"]
    if "states" in value:
        import aws_sdk_inspector.types.assessment_run_state_list

        out["states"] = (
            aws_sdk_inspector.types.assessment_run_state_list.serialize_aws_json_1_1(
                value["states"]
            )
        )
    if "duration_range" in value:
        import aws_sdk_inspector.types.duration_range

        out["durationRange"] = (
            aws_sdk_inspector.types.duration_range.serialize_aws_json_1_1(
                value["duration_range"]
            )
        )
    if "rules_package_arns" in value:
        import aws_sdk_inspector.types.filter_rules_package_arn_list

        out["rulesPackageArns"] = (
            aws_sdk_inspector.types.filter_rules_package_arn_list.serialize_aws_json_1_1(
                value["rules_package_arns"]
            )
        )
    if "start_time_range" in value:
        import aws_sdk_inspector.types.timestamp_range

        out["startTimeRange"] = (
            aws_sdk_inspector.types.timestamp_range.serialize_aws_json_1_1(
                value["start_time_range"]
            )
        )
    if "completion_time_range" in value:
        import aws_sdk_inspector.types.timestamp_range

        out["completionTimeRange"] = (
            aws_sdk_inspector.types.timestamp_range.serialize_aws_json_1_1(
                value["completion_time_range"]
            )
        )
    if "state_change_time_range" in value:
        import aws_sdk_inspector.types.timestamp_range

        out["stateChangeTimeRange"] = (
            aws_sdk_inspector.types.timestamp_range.serialize_aws_json_1_1(
                value["state_change_time_range"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunFilter:
    out: AssessmentRunFilter = {}  # type: ignore[typeddict-item]
    if "namePattern" in data:
        out["name_pattern"] = data["namePattern"]
    if "states" in data:
        import aws_sdk_inspector.types.assessment_run_state_list

        out["states"] = (
            aws_sdk_inspector.types.assessment_run_state_list.deserialize_aws_json_1_1(
                data["states"]
            )
        )
    if "durationRange" in data:
        import aws_sdk_inspector.types.duration_range

        out["duration_range"] = (
            aws_sdk_inspector.types.duration_range.deserialize_aws_json_1_1(
                data["durationRange"]
            )
        )
    if "rulesPackageArns" in data:
        import aws_sdk_inspector.types.filter_rules_package_arn_list

        out["rules_package_arns"] = (
            aws_sdk_inspector.types.filter_rules_package_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    if "startTimeRange" in data:
        import aws_sdk_inspector.types.timestamp_range

        out["start_time_range"] = (
            aws_sdk_inspector.types.timestamp_range.deserialize_aws_json_1_1(
                data["startTimeRange"]
            )
        )
    if "completionTimeRange" in data:
        import aws_sdk_inspector.types.timestamp_range

        out["completion_time_range"] = (
            aws_sdk_inspector.types.timestamp_range.deserialize_aws_json_1_1(
                data["completionTimeRange"]
            )
        )
    if "stateChangeTimeRange" in data:
        import aws_sdk_inspector.types.timestamp_range

        out["state_change_time_range"] = (
            aws_sdk_inspector.types.timestamp_range.deserialize_aws_json_1_1(
                data["stateChangeTimeRange"]
            )
        )
    return out
