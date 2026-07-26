"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.harness_arn
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_status


class HarnessSummary(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness.</p>"""
    harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the harness.</p>"""
    arn: "capo_bedrock_agentcore_control.types.harness_arn.HarnessArn"
    """<p>The ARN of the harness.</p>"""
    status: "capo_bedrock_agentcore_control.types.harness_status.HarnessStatus"
    """<p>The current status of the harness.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the harness was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the harness was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSummary) -> dict:
    out: dict = {}
    out["harnessId"] = value["harness_id"]
    out["harnessName"] = value["harness_name"]
    out["arn"] = value["arn"]
    import capo_bedrock_agentcore_control.types.harness_status

    out["status"] = capo_bedrock_agentcore_control.types.harness_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessSummary:
    out: HarnessSummary = {}  # type: ignore[typeddict-item]
    if "harnessId" in data:
        out["harness_id"] = data["harnessId"]
    else:
        raise DeserializationError("HarnessSummary.harness_id required")
    if "harnessName" in data:
        out["harness_name"] = data["harnessName"]
    else:
        raise DeserializationError("HarnessSummary.harness_name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("HarnessSummary.arn required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.harness_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.harness_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("HarnessSummary.status required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("HarnessSummary.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("HarnessSummary.updated_at required")
    return out
