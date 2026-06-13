"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaAnalysisRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.schema_analysis_rule_request_list


class BatchGetSchemaAnalysisRuleInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique identifier of the collaboration that contains the schema analysis rule.</p>"""
    schema_analysis_rule_requests: "aws_sdk_cleanrooms.types.schema_analysis_rule_request_list.SchemaAnalysisRuleRequestList"
    """<p>The information that's necessary to retrieve a schema analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaAnalysisRuleInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.schema_analysis_rule_request_list

    out["schemaAnalysisRuleRequests"] = (
        aws_sdk_cleanrooms.types.schema_analysis_rule_request_list.serialize_json(
            value["schema_analysis_rule_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSchemaAnalysisRuleInput:
    out: BatchGetSchemaAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if "schemaAnalysisRuleRequests" in data:
        import aws_sdk_cleanrooms.types.schema_analysis_rule_request_list

        out["schema_analysis_rule_requests"] = (
            aws_sdk_cleanrooms.types.schema_analysis_rule_request_list.deserialize_json(
                data["schemaAnalysisRuleRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetSchemaAnalysisRuleInput.schema_analysis_rule_requests required"
        )
    return out
