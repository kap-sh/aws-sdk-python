"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.rules_max_results
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.whole_number_version_string


class GetRulesRequest(TypedDict, closed=True):
    rule_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The rule ID.</p>"""
    detector_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The detector ID.</p>"""
    rule_version: NotRequired[
        "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The rule version.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token.</p>"""
    max_results: NotRequired[
        "aws_sdk_frauddetector.types.rules_max_results.RulesMaxResults"
    ]
    """<p>The maximum number of rules to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRulesRequest) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    out["detectorId"] = value["detector_id"]
    if "rule_version" in value:
        out["ruleVersion"] = value["rule_version"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRulesRequest:
    out: GetRulesRequest = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("GetRulesRequest.detector_id required")
    if "ruleVersion" in data:
        out["rule_version"] = data["ruleVersion"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
