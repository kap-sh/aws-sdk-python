"""Generated from Smithy shape ``com.amazonaws.frauddetector#Rule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.whole_number_version_string


class Rule(TypedDict):
    detector_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The detector for which the rule is associated.</p>"""
    rule_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The rule ID.</p>"""
    rule_version: "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    """<p>The rule version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["ruleId"] = value["rule_id"]
    out["ruleVersion"] = value["rule_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("Rule.detector_id required")
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("Rule.rule_id required")
    if "ruleVersion" in data:
        out["rule_version"] = data["ruleVersion"]
    else:
        raise DeserializationError("Rule.rule_version required")
    return out
