"""Generated from Smithy shape ``com.amazonaws.amp#AlertManagerDefinitionDescription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_amp.types.alert_manager_definition_data
    import aws_sdk_amp.types.alert_manager_definition_status


class AlertManagerDefinitionDescription(TypedDict):
    status: (
        "aws_sdk_amp.types.alert_manager_definition_status.AlertManagerDefinitionStatus"
    )
    """<p>A structure that displays the current status of the alert manager definition..</p>"""
    data: "aws_sdk_amp.types.alert_manager_definition_data.AlertManagerDefinitionData"
    r"""<p>The actual alert manager definition.</p> <p>For details about the alert manager definition, see <a href=\"https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html\">AlertManagedDefinitionData</a>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the alert manager definition was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time that the alert manager definition was most recently changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlertManagerDefinitionDescription) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.alert_manager_definition_status

    out["status"] = aws_sdk_amp.types.alert_manager_definition_status.serialize_json(
        value["status"]
    )
    import aws_sdk_amp.types.alert_manager_definition_data

    out["data"] = aws_sdk_amp.types.alert_manager_definition_data.serialize_json(
        value["data"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["createdAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> AlertManagerDefinitionDescription:
    out: AlertManagerDefinitionDescription = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_amp.types.alert_manager_definition_status

        out["status"] = (
            aws_sdk_amp.types.alert_manager_definition_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AlertManagerDefinitionDescription.status required")
    if "data" in data:
        import aws_sdk_amp.types.alert_manager_definition_data

        out["data"] = aws_sdk_amp.types.alert_manager_definition_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("AlertManagerDefinitionDescription.data required")
    if "createdAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["created_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "AlertManagerDefinitionDescription.created_at required"
        )
    if "modifiedAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["modified_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError(
            "AlertManagerDefinitionDescription.modified_at required"
        )
    return out
