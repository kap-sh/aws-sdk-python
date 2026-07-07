"""Generated from Smithy shape ``com.amazonaws.ssmsap#RuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.rule_result_id
    import aws_sdk_ssm_sap.types.rule_result_metadata
    import aws_sdk_ssm_sap.types.rule_result_status


class RuleResult(TypedDict, closed=True):
    id: NotRequired["aws_sdk_ssm_sap.types.rule_result_id.RuleResultId"]
    """<p>The unique identifier of the rule result.</p>"""
    description: NotRequired["str"]
    """<p>A description of what the rule validates.</p>"""
    status: NotRequired["aws_sdk_ssm_sap.types.rule_result_status.RuleResultStatus"]
    """<p>The status of the rule result.</p>"""
    message: NotRequired["str"]
    """<p>A message providing details about the rule result.</p>"""
    metadata: NotRequired[
        "aws_sdk_ssm_sap.types.rule_result_metadata.RuleResultMetadata"
    ]
    """<p>Additional metadata associated with the rule result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleResult) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_ssm_sap.types.rule_result_status

        out["Status"] = aws_sdk_ssm_sap.types.rule_result_status.serialize_json(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "metadata" in value:
        import aws_sdk_ssm_sap.types.rule_result_metadata

        out["Metadata"] = aws_sdk_ssm_sap.types.rule_result_metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> RuleResult:
    out: RuleResult = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_ssm_sap.types.rule_result_status

        out["status"] = aws_sdk_ssm_sap.types.rule_result_status.deserialize_json(
            data["Status"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Metadata" in data:
        import aws_sdk_ssm_sap.types.rule_result_metadata

        out["metadata"] = aws_sdk_ssm_sap.types.rule_result_metadata.deserialize_json(
            data["Metadata"]
        )
    return out
