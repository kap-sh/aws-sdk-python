"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelEnforcement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.excluded_models_list
    import aws_sdk_bedrock.types.included_models_list


class ModelEnforcement(TypedDict, closed=True):
    included_models: "aws_sdk_bedrock.types.included_models_list.IncludedModelsList"
    """<p>Models to enforce the guardrail on.</p>"""
    excluded_models: "aws_sdk_bedrock.types.excluded_models_list.ExcludedModelsList"
    """<p>Models to exclude from enforcement of the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelEnforcement) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.included_models_list

    out["includedModels"] = aws_sdk_bedrock.types.included_models_list.serialize_json(
        value["included_models"]
    )
    import aws_sdk_bedrock.types.excluded_models_list

    out["excludedModels"] = aws_sdk_bedrock.types.excluded_models_list.serialize_json(
        value["excluded_models"]
    )
    return out


def deserialize_json(data: dict) -> ModelEnforcement:
    out: ModelEnforcement = {}  # type: ignore[typeddict-item]
    if "includedModels" in data:
        import aws_sdk_bedrock.types.included_models_list

        out["included_models"] = (
            aws_sdk_bedrock.types.included_models_list.deserialize_json(
                data["includedModels"]
            )
        )
    else:
        raise DeserializationError("ModelEnforcement.included_models required")
    if "excludedModels" in data:
        import aws_sdk_bedrock.types.excluded_models_list

        out["excluded_models"] = (
            aws_sdk_bedrock.types.excluded_models_list.deserialize_json(
                data["excludedModels"]
            )
        )
    else:
        raise DeserializationError("ModelEnforcement.excluded_models required")
    return out
