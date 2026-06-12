"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetDetectorVersionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.detector_version_status
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.list_of_model_versions
    import aws_sdk_frauddetector.types.list_of_strings
    import aws_sdk_frauddetector.types.rule_execution_mode
    import aws_sdk_frauddetector.types.rule_list
    import aws_sdk_frauddetector.types.time
    import aws_sdk_frauddetector.types.whole_number_version_string


class GetDetectorVersionResult(TypedDict):
    detector_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The detector ID.</p>"""
    detector_version_id: NotRequired[
        "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The detector version ID.</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p>The detector version description.</p>"""
    external_model_endpoints: NotRequired[
        "aws_sdk_frauddetector.types.list_of_strings.ListOfStrings"
    ]
    """<p>The Amazon SageMaker model endpoints included in the detector version.</p>"""
    model_versions: NotRequired[
        "aws_sdk_frauddetector.types.list_of_model_versions.ListOfModelVersions"
    ]
    """<p>The model versions included in the detector version. </p>"""
    rules: NotRequired["aws_sdk_frauddetector.types.rule_list.RuleList"]
    """<p>The rules included in the detector version.</p>"""
    status: NotRequired[
        "aws_sdk_frauddetector.types.detector_version_status.DetectorVersionStatus"
    ]
    """<p>The status of the detector version.</p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The timestamp when the detector version was last updated. </p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The timestamp when the detector version was created. </p>"""
    rule_execution_mode: NotRequired[
        "aws_sdk_frauddetector.types.rule_execution_mode.RuleExecutionMode"
    ]
    """<p>The execution mode of the rule in the dectector</p> <p> <code>FIRST_MATCHED</code> indicates that Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.</p> <p> <code>ALL_MATCHED</code> indicates that Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. You can define and edit the rule mode at the detector version level, when it is in draft status.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The detector version ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDetectorVersionResult) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_version_id" in value:
        out["detectorVersionId"] = value["detector_version_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "external_model_endpoints" in value:
        import aws_sdk_frauddetector.types.list_of_strings

        out["externalModelEndpoints"] = (
            aws_sdk_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["external_model_endpoints"]
            )
        )
    if "model_versions" in value:
        import aws_sdk_frauddetector.types.list_of_model_versions

        out["modelVersions"] = (
            aws_sdk_frauddetector.types.list_of_model_versions.serialize_aws_json_1_1(
                value["model_versions"]
            )
        )
    if "rules" in value:
        import aws_sdk_frauddetector.types.rule_list

        out["rules"] = aws_sdk_frauddetector.types.rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    if "status" in value:
        import aws_sdk_frauddetector.types.detector_version_status

        out["status"] = (
            aws_sdk_frauddetector.types.detector_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "rule_execution_mode" in value:
        import aws_sdk_frauddetector.types.rule_execution_mode

        out["ruleExecutionMode"] = (
            aws_sdk_frauddetector.types.rule_execution_mode.serialize_aws_json_1_1(
                value["rule_execution_mode"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDetectorVersionResult:
    out: GetDetectorVersionResult = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    if "description" in data:
        out["description"] = data["description"]
    if "externalModelEndpoints" in data:
        import aws_sdk_frauddetector.types.list_of_strings

        out["external_model_endpoints"] = (
            aws_sdk_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["externalModelEndpoints"]
            )
        )
    if "modelVersions" in data:
        import aws_sdk_frauddetector.types.list_of_model_versions

        out["model_versions"] = (
            aws_sdk_frauddetector.types.list_of_model_versions.deserialize_aws_json_1_1(
                data["modelVersions"]
            )
        )
    if "rules" in data:
        import aws_sdk_frauddetector.types.rule_list

        out["rules"] = aws_sdk_frauddetector.types.rule_list.deserialize_aws_json_1_1(
            data["rules"]
        )
    if "status" in data:
        import aws_sdk_frauddetector.types.detector_version_status

        out["status"] = (
            aws_sdk_frauddetector.types.detector_version_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "ruleExecutionMode" in data:
        import aws_sdk_frauddetector.types.rule_execution_mode

        out["rule_execution_mode"] = (
            aws_sdk_frauddetector.types.rule_execution_mode.deserialize_aws_json_1_1(
                data["ruleExecutionMode"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
