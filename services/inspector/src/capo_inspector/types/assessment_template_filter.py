"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentTemplateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.duration_range
    import capo_inspector.types.filter_rules_package_arn_list
    import capo_inspector.types.name_pattern


class AssessmentTemplateFilter(TypedDict, closed=True):
    name_pattern: NotRequired["capo_inspector.types.name_pattern.NamePattern"]
    """<p>For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the <b>assessmentTemplateName</b> property of the <a>AssessmentTemplate</a> data type.</p>"""
    duration_range: NotRequired["capo_inspector.types.duration_range.DurationRange"]
    """<p>For a record to match a filter, the value specified for this data type property must inclusively match any value between the specified minimum and maximum values of the <b>durationInSeconds</b> property of the <a>AssessmentTemplate</a> data type.</p>"""
    rules_package_arns: NotRequired[
        "capo_inspector.types.filter_rules_package_arn_list.FilterRulesPackageArnList"
    ]
    """<p>For a record to match a filter, the values that are specified for this data type property must be contained in the list of values of the <b>rulesPackageArns</b> property of the <a>AssessmentTemplate</a> data type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentTemplateFilter) -> dict:
    out: dict = {}
    if "name_pattern" in value:
        out["namePattern"] = value["name_pattern"]
    if "duration_range" in value:
        import capo_inspector.types.duration_range

        out["durationRange"] = (
            capo_inspector.types.duration_range.serialize_aws_json_1_1(
                value["duration_range"]
            )
        )
    if "rules_package_arns" in value:
        import capo_inspector.types.filter_rules_package_arn_list

        out["rulesPackageArns"] = (
            capo_inspector.types.filter_rules_package_arn_list.serialize_aws_json_1_1(
                value["rules_package_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentTemplateFilter:
    out: AssessmentTemplateFilter = {}  # type: ignore[typeddict-item]
    if "namePattern" in data:
        out["name_pattern"] = data["namePattern"]
    if "durationRange" in data:
        import capo_inspector.types.duration_range

        out["duration_range"] = (
            capo_inspector.types.duration_range.deserialize_aws_json_1_1(
                data["durationRange"]
            )
        )
    if "rulesPackageArns" in data:
        import capo_inspector.types.filter_rules_package_arn_list

        out["rules_package_arns"] = (
            capo_inspector.types.filter_rules_package_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    return out
