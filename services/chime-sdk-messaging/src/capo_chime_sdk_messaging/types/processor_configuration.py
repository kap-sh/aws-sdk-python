"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ProcessorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.lambda_configuration

ProcessorConfiguration = TypedDict(
    "ProcessorConfiguration",
    {
        "lambda": "capo_chime_sdk_messaging.types.lambda_configuration.LambdaConfiguration",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ProcessorConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.lambda_configuration

    out["Lambda"] = capo_chime_sdk_messaging.types.lambda_configuration.serialize_json(
        value["lambda"]
    )
    return out


def deserialize_json(data: dict) -> ProcessorConfiguration:
    out: ProcessorConfiguration = {}  # type: ignore[typeddict-item]
    if "Lambda" in data:
        import capo_chime_sdk_messaging.types.lambda_configuration

        out["lambda"] = (
            capo_chime_sdk_messaging.types.lambda_configuration.deserialize_json(
                data["Lambda"]
            )
        )
    else:
        raise DeserializationError("ProcessorConfiguration.lambda required")
    return out
