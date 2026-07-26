"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.code_security_integration_arn
    import capo_inspector2.types.integration_name
    import capo_inspector2.types.integration_status
    import capo_inspector2.types.integration_type
    import capo_inspector2.types.tag_map


class CodeSecurityIntegrationSummary(TypedDict, closed=True):
    integration_arn: (
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the code security integration.</p>"""
    name: "capo_inspector2.types.integration_name.IntegrationName"
    """<p>The name of the code security integration.</p>"""
    type: "capo_inspector2.types.integration_type.IntegrationType"
    """<p>The type of repository provider for the integration.</p>"""
    status: "capo_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the code security integration.</p>"""
    status_reason: "str"
    """<p>The reason for the current status of the code security integration.</p>"""
    created_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was created.</p>"""
    last_update_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was last updated.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the code security integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityIntegrationSummary) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    out["name"] = value["name"]
    import capo_inspector2.types.integration_type

    out["type"] = capo_inspector2.types.integration_type.serialize_json(value["type"])
    import capo_inspector2.types.integration_status

    out["status"] = capo_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    out["statusReason"] = value["status_reason"]
    import capo_inspector2.types._prelude.timestamp

    out["createdOn"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["created_on"]
    )
    import capo_inspector2.types._prelude.timestamp

    out["lastUpdateOn"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["last_update_on"]
    )
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CodeSecurityIntegrationSummary:
    out: CodeSecurityIntegrationSummary = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "CodeSecurityIntegrationSummary.integration_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CodeSecurityIntegrationSummary.name required")
    if "type" in data:
        import capo_inspector2.types.integration_type

        out["type"] = capo_inspector2.types.integration_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CodeSecurityIntegrationSummary.type required")
    if "status" in data:
        import capo_inspector2.types.integration_status

        out["status"] = capo_inspector2.types.integration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CodeSecurityIntegrationSummary.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    else:
        raise DeserializationError(
            "CodeSecurityIntegrationSummary.status_reason required"
        )
    if "createdOn" in data:
        import capo_inspector2.types._prelude.timestamp

        out["created_on"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["createdOn"]
        )
    else:
        raise DeserializationError("CodeSecurityIntegrationSummary.created_on required")
    if "lastUpdateOn" in data:
        import capo_inspector2.types._prelude.timestamp

        out["last_update_on"] = (
            capo_inspector2.types._prelude.timestamp.deserialize_json(
                data["lastUpdateOn"]
            )
        )
    else:
        raise DeserializationError(
            "CodeSecurityIntegrationSummary.last_update_on required"
        )
    if "tags" in data:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
