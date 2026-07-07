"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CustomEntityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.custom_data_identifier_list


class CustomEntityConfig(TypedDict, closed=True):
    custom_data_identifiers: "aws_sdk_cleanroomsml.types.custom_data_identifier_list.CustomDataIdentifierList"
    """<p>Defines data identifiers for the custom entity configuration. Provide this only if CUSTOM redaction is configured. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomEntityConfig) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.custom_data_identifier_list

    out["customDataIdentifiers"] = (
        aws_sdk_cleanroomsml.types.custom_data_identifier_list.serialize_json(
            value["custom_data_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomEntityConfig:
    out: CustomEntityConfig = {}  # type: ignore[typeddict-item]
    if "customDataIdentifiers" in data:
        import aws_sdk_cleanroomsml.types.custom_data_identifier_list

        out["custom_data_identifiers"] = (
            aws_sdk_cleanroomsml.types.custom_data_identifier_list.deserialize_json(
                data["customDataIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "CustomEntityConfig.custom_data_identifiers required"
        )
    return out
