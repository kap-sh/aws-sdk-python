"""Generated from Smithy shape ``com.amazonaws.mq#Configurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__list_of_configuration_id
    import aws_sdk_mq.types.configuration_id


class Configurations(TypedDict, closed=True):
    current: NotRequired["aws_sdk_mq.types.configuration_id.ConfigurationId"]
    """<p>The broker's current configuration.</p>"""
    history: NotRequired[
        "aws_sdk_mq.types.__list_of_configuration_id.__listOfConfigurationId"
    ]
    """<p>The history of configurations applied to the broker.</p>"""
    pending: NotRequired["aws_sdk_mq.types.configuration_id.ConfigurationId"]
    """<p>The broker's pending configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configurations) -> dict:
    out: dict = {}
    if "current" in value:
        import aws_sdk_mq.types.configuration_id

        out["current"] = aws_sdk_mq.types.configuration_id.serialize_json(
            value["current"]
        )
    if "history" in value:
        import aws_sdk_mq.types.__list_of_configuration_id

        out["history"] = aws_sdk_mq.types.__list_of_configuration_id.serialize_json(
            value["history"]
        )
    if "pending" in value:
        import aws_sdk_mq.types.configuration_id

        out["pending"] = aws_sdk_mq.types.configuration_id.serialize_json(
            value["pending"]
        )
    return out


def deserialize_json(data: dict) -> Configurations:
    out: Configurations = {}  # type: ignore[typeddict-item]
    if "current" in data:
        import aws_sdk_mq.types.configuration_id

        out["current"] = aws_sdk_mq.types.configuration_id.deserialize_json(
            data["current"]
        )
    if "history" in data:
        import aws_sdk_mq.types.__list_of_configuration_id

        out["history"] = aws_sdk_mq.types.__list_of_configuration_id.deserialize_json(
            data["history"]
        )
    if "pending" in data:
        import aws_sdk_mq.types.configuration_id

        out["pending"] = aws_sdk_mq.types.configuration_id.deserialize_json(
            data["pending"]
        )
    return out
