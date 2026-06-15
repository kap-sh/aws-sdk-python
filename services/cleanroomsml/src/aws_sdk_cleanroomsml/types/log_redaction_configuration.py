"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogRedactionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.custom_entity_config
    import aws_sdk_cleanroomsml.types.entity_type_list


class LogRedactionConfiguration(TypedDict):
    entities_to_redact: "aws_sdk_cleanroomsml.types.entity_type_list.EntityTypeList"
    r"""<p>Specifies the entities to be redacted from logs. Entities to redact are \"ALL_PERSONALLY_IDENTIFIABLE_INFORMATION\", \"NUMBERS\",\"CUSTOM\". If CUSTOM is supplied or configured, custom patterns (customDataIdentifiers) should be provided, and the patterns will be redacted in logs or error messages.</p>"""
    custom_entity_config: NotRequired[
        "aws_sdk_cleanroomsml.types.custom_entity_config.CustomEntityConfig"
    ]
    """<p>Specifies the configuration for custom entities in the context of log redaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogRedactionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.entity_type_list

    out["entitiesToRedact"] = (
        aws_sdk_cleanroomsml.types.entity_type_list.serialize_json(
            value["entities_to_redact"]
        )
    )
    if "custom_entity_config" in value:
        import aws_sdk_cleanroomsml.types.custom_entity_config

        out["customEntityConfig"] = (
            aws_sdk_cleanroomsml.types.custom_entity_config.serialize_json(
                value["custom_entity_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogRedactionConfiguration:
    out: LogRedactionConfiguration = {}  # type: ignore[typeddict-item]
    if "entitiesToRedact" in data:
        import aws_sdk_cleanroomsml.types.entity_type_list

        out["entities_to_redact"] = (
            aws_sdk_cleanroomsml.types.entity_type_list.deserialize_json(
                data["entitiesToRedact"]
            )
        )
    else:
        raise DeserializationError(
            "LogRedactionConfiguration.entities_to_redact required"
        )
    if "customEntityConfig" in data:
        import aws_sdk_cleanroomsml.types.custom_entity_config

        out["custom_entity_config"] = (
            aws_sdk_cleanroomsml.types.custom_entity_config.deserialize_json(
                data["customEntityConfig"]
            )
        )
    return out
