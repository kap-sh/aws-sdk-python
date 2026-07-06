"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MigrationAlert``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.migration_alert_details
    import aws_sdk_lex_model_building_service.types.migration_alert_message
    import aws_sdk_lex_model_building_service.types.migration_alert_reference_ur_ls
    import aws_sdk_lex_model_building_service.types.migration_alert_type


class MigrationAlert(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_alert_type.MigrationAlertType"
    ]
    """<p>The type of alert. There are two kinds of alerts:</p> <ul> <li> <p> <code>ERROR</code> - There was an issue with the migration that can't be resolved. The migration stops.</p> </li> <li> <p> <code>WARN</code> - There was an issue with the migration that requires manual changes to the new Amazon Lex V2 bot. The migration continues.</p> </li> </ul>"""
    message: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_alert_message.MigrationAlertMessage"
    ]
    """<p>A message that describes why the alert was issued.</p>"""
    details: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_alert_details.MigrationAlertDetails"
    ]
    """<p>Additional details about the alert.</p>"""
    reference_ur_ls: NotRequired[
        "aws_sdk_lex_model_building_service.types.migration_alert_reference_ur_ls.MigrationAlertReferenceURLs"
    ]
    """<p>A link to the Amazon Lex documentation that describes how to resolve the alert.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationAlert) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_lex_model_building_service.types.migration_alert_type

        out["type"] = (
            aws_sdk_lex_model_building_service.types.migration_alert_type.serialize_json(
                value["type"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "details" in value:
        import aws_sdk_lex_model_building_service.types.migration_alert_details

        out["details"] = (
            aws_sdk_lex_model_building_service.types.migration_alert_details.serialize_json(
                value["details"]
            )
        )
    if "reference_ur_ls" in value:
        import aws_sdk_lex_model_building_service.types.migration_alert_reference_ur_ls

        out["referenceURLs"] = (
            aws_sdk_lex_model_building_service.types.migration_alert_reference_ur_ls.serialize_json(
                value["reference_ur_ls"]
            )
        )
    return out


def deserialize_json(data: dict) -> MigrationAlert:
    out: MigrationAlert = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_lex_model_building_service.types.migration_alert_type

        out["type"] = (
            aws_sdk_lex_model_building_service.types.migration_alert_type.deserialize_json(
                data["type"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    if "details" in data:
        import aws_sdk_lex_model_building_service.types.migration_alert_details

        out["details"] = (
            aws_sdk_lex_model_building_service.types.migration_alert_details.deserialize_json(
                data["details"]
            )
        )
    if "referenceURLs" in data:
        import aws_sdk_lex_model_building_service.types.migration_alert_reference_ur_ls

        out["reference_ur_ls"] = (
            aws_sdk_lex_model_building_service.types.migration_alert_reference_ur_ls.deserialize_json(
                data["referenceURLs"]
            )
        )
    return out
