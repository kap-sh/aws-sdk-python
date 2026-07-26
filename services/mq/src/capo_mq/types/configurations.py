"""Generated from Smithy shape ``com.amazonaws.mq#Configurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__list_of_configuration_id
    import capo_mq.types.configuration_id


class Configurations(TypedDict, closed=True):
    current: NotRequired["capo_mq.types.configuration_id.ConfigurationId"]
    """<p>The broker's current configuration.</p>"""
    history: NotRequired[
        "capo_mq.types.__list_of_configuration_id.__listOfConfigurationId"
    ]
    """<p>The history of configurations applied to the broker.</p>"""
    pending: NotRequired["capo_mq.types.configuration_id.ConfigurationId"]
    """<p>The broker's pending configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configurations) -> dict:
    out: dict = {}
    if "current" in value:
        import capo_mq.types.configuration_id

        out["current"] = capo_mq.types.configuration_id.serialize_json(value["current"])
    if "history" in value:
        import capo_mq.types.__list_of_configuration_id

        out["history"] = capo_mq.types.__list_of_configuration_id.serialize_json(
            value["history"]
        )
    if "pending" in value:
        import capo_mq.types.configuration_id

        out["pending"] = capo_mq.types.configuration_id.serialize_json(value["pending"])
    return out


def deserialize_json(data: dict) -> Configurations:
    out: Configurations = {}  # type: ignore[typeddict-item]
    if "current" in data:
        import capo_mq.types.configuration_id

        out["current"] = capo_mq.types.configuration_id.deserialize_json(
            data["current"]
        )
    if "history" in data:
        import capo_mq.types.__list_of_configuration_id

        out["history"] = capo_mq.types.__list_of_configuration_id.deserialize_json(
            data["history"]
        )
    if "pending" in data:
        import capo_mq.types.configuration_id

        out["pending"] = capo_mq.types.configuration_id.deserialize_json(
            data["pending"]
        )
    return out
