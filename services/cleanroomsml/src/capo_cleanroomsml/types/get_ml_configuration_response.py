"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetMLConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.ml_output_configuration
    import capo_cleanroomsml.types.uuid


class GetMLConfigurationResponse(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that owns the ML configuration you requested.</p>"""
    default_output_location: (
        "capo_cleanroomsml.types.ml_output_configuration.MLOutputConfiguration"
    )
    """<p>The Amazon S3 location where ML model output is stored.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the ML configuration was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ML configuration was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLConfigurationResponse) -> dict:
    out: dict = {}
    out["membershipIdentifier"] = value["membership_identifier"]
    import capo_cleanroomsml.types.ml_output_configuration

    out["defaultOutputLocation"] = (
        capo_cleanroomsml.types.ml_output_configuration.serialize_json(
            value["default_output_location"]
        )
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> GetMLConfigurationResponse:
    out: GetMLConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "GetMLConfigurationResponse.membership_identifier required"
        )
    if "defaultOutputLocation" in data:
        import capo_cleanroomsml.types.ml_output_configuration

        out["default_output_location"] = (
            capo_cleanroomsml.types.ml_output_configuration.deserialize_json(
                data["defaultOutputLocation"]
            )
        )
    else:
        raise DeserializationError(
            "GetMLConfigurationResponse.default_output_location required"
        )
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("GetMLConfigurationResponse.create_time required")
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("GetMLConfigurationResponse.update_time required")
    return out
