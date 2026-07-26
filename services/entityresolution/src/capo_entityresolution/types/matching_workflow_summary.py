"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchingWorkflowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.matching_workflow_arn
    import capo_entityresolution.types.resolution_type


class MatchingWorkflowSummary(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    workflow_arn: (
        "capo_entityresolution.types.matching_workflow_arn.MatchingWorkflowArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>MatchingWorkflow</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the workflow was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the workflow was last updated.</p>"""
    resolution_type: "capo_entityresolution.types.resolution_type.ResolutionType"
    """<p>The method that has been specified for data matching, either using matching provided by Entity Resolution or through a provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingWorkflowSummary) -> dict:
    out: dict = {}
    out["workflowName"] = value["workflow_name"]
    out["workflowArn"] = value["workflow_arn"]
    import capo_entityresolution.types._prelude.timestamp

    out["createdAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["updatedAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    import capo_entityresolution.types.resolution_type

    out["resolutionType"] = capo_entityresolution.types.resolution_type.serialize_json(
        value["resolution_type"]
    )
    return out


def deserialize_json(data: dict) -> MatchingWorkflowSummary:
    out: MatchingWorkflowSummary = {}  # type: ignore[typeddict-item]
    if "workflowName" in data:
        out["workflow_name"] = data["workflowName"]
    else:
        raise DeserializationError("MatchingWorkflowSummary.workflow_name required")
    if "workflowArn" in data:
        out["workflow_arn"] = data["workflowArn"]
    else:
        raise DeserializationError("MatchingWorkflowSummary.workflow_arn required")
    if "createdAt" in data:
        import capo_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("MatchingWorkflowSummary.created_at required")
    if "updatedAt" in data:
        import capo_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("MatchingWorkflowSummary.updated_at required")
    if "resolutionType" in data:
        import capo_entityresolution.types.resolution_type

        out["resolution_type"] = (
            capo_entityresolution.types.resolution_type.deserialize_json(
                data["resolutionType"]
            )
        )
    else:
        raise DeserializationError("MatchingWorkflowSummary.resolution_type required")
    return out
