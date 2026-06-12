"""Generated from Smithy shape ``com.amazonaws.frauddetector#RuleDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.language
    import aws_sdk_frauddetector.types.non_empty_list_of_strings
    import aws_sdk_frauddetector.types.rule_expression
    import aws_sdk_frauddetector.types.time
    import aws_sdk_frauddetector.types.whole_number_version_string


class RuleDetail(TypedDict):
    rule_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The rule ID.</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p>The rule description.</p>"""
    detector_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The detector for which the rule is associated.</p>"""
    rule_version: NotRequired[
        "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The rule version.</p>"""
    expression: NotRequired[
        "aws_sdk_frauddetector.types.rule_expression.ruleExpression"
    ]
    """<p>The rule expression.</p>"""
    language: NotRequired["aws_sdk_frauddetector.types.language.Language"]
    """<p>The rule language.</p>"""
    outcomes: NotRequired[
        "aws_sdk_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    ]
    """<p>The rule outcomes.</p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of the last time the rule was updated.</p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The timestamp of when the rule was created.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The rule ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleDetail) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "rule_version" in value:
        out["ruleVersion"] = value["rule_version"]
    if "expression" in value:
        out["expression"] = value["expression"]
    if "language" in value:
        import aws_sdk_frauddetector.types.language

        out["language"] = aws_sdk_frauddetector.types.language.serialize_aws_json_1_1(
            value["language"]
        )
    if "outcomes" in value:
        import aws_sdk_frauddetector.types.non_empty_list_of_strings

        out["outcomes"] = (
            aws_sdk_frauddetector.types.non_empty_list_of_strings.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleDetail:
    out: RuleDetail = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    if "description" in data:
        out["description"] = data["description"]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "ruleVersion" in data:
        out["rule_version"] = data["ruleVersion"]
    if "expression" in data:
        out["expression"] = data["expression"]
    if "language" in data:
        import aws_sdk_frauddetector.types.language

        out["language"] = aws_sdk_frauddetector.types.language.deserialize_aws_json_1_1(
            data["language"]
        )
    if "outcomes" in data:
        import aws_sdk_frauddetector.types.non_empty_list_of_strings

        out["outcomes"] = (
            aws_sdk_frauddetector.types.non_empty_list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
