"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#QInConnectIntentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.q_in_connect_assistant_configuration


class QInConnectIntentConfiguration(TypedDict):
    q_in_connect_assistant_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.q_in_connect_assistant_configuration.QInConnectAssistantConfiguration"
    ]
    """<p>The Qinconnect assistant configuration details of the Qinconnect intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QInConnectIntentConfiguration) -> dict:
    out: dict = {}
    if "q_in_connect_assistant_configuration" in value:
        import aws_sdk_lex_models_v2.types.q_in_connect_assistant_configuration

        out["qInConnectAssistantConfiguration"] = (
            aws_sdk_lex_models_v2.types.q_in_connect_assistant_configuration.serialize_json(
                value["q_in_connect_assistant_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> QInConnectIntentConfiguration:
    out: QInConnectIntentConfiguration = {}  # type: ignore[typeddict-item]
    if "qInConnectAssistantConfiguration" in data:
        import aws_sdk_lex_models_v2.types.q_in_connect_assistant_configuration

        out["q_in_connect_assistant_configuration"] = (
            aws_sdk_lex_models_v2.types.q_in_connect_assistant_configuration.deserialize_json(
                data["qInConnectAssistantConfiguration"]
            )
        )
    return out
