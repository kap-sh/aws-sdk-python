"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailContentPolicyConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_content_filters_config


class AIGuardrailContentPolicyConfig(TypedDict):
    filters_config: "aws_sdk_qconnect.types.guardrail_content_filters_config.GuardrailContentFiltersConfig"
    """<p>Contains the type of the content filter and how strongly it should apply to prompts and model responses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailContentPolicyConfig) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.guardrail_content_filters_config

    out["filtersConfig"] = (
        aws_sdk_qconnect.types.guardrail_content_filters_config.serialize_json(
            value["filters_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> AIGuardrailContentPolicyConfig:
    out: AIGuardrailContentPolicyConfig = {}  # type: ignore[typeddict-item]
    if "filtersConfig" in data:
        import aws_sdk_qconnect.types.guardrail_content_filters_config

        out["filters_config"] = (
            aws_sdk_qconnect.types.guardrail_content_filters_config.deserialize_json(
                data["filtersConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AIGuardrailContentPolicyConfig.filters_config required"
        )
    return out
