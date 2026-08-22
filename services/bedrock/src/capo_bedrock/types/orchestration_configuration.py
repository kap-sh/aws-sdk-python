"""Generated from Smithy shape ``com.amazonaws.bedrock#OrchestrationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.query_transformation_configuration


class OrchestrationConfiguration(TypedDict, closed=True):
    query_transformation_configuration: "capo_bedrock.types.query_transformation_configuration.QueryTransformationConfiguration"
    """<p>Contains configuration details for transforming the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock.types.query_transformation_configuration

    out["queryTransformationConfiguration"] = (
        capo_bedrock.types.query_transformation_configuration.serialize_json(
            value["query_transformation_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> OrchestrationConfiguration:
    out: OrchestrationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("queryTransformationConfiguration") is not None:
        import capo_bedrock.types.query_transformation_configuration

        out["query_transformation_configuration"] = (
            capo_bedrock.types.query_transformation_configuration.deserialize_json(
                data["queryTransformationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "OrchestrationConfiguration.query_transformation_configuration required"
        )
    return out
