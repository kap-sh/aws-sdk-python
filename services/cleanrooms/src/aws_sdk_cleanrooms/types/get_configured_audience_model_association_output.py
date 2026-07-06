"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetConfiguredAudienceModelAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_audience_model_association


class GetConfiguredAudienceModelAssociationOutput(TypedDict, closed=True):
    configured_audience_model_association: "aws_sdk_cleanrooms.types.configured_audience_model_association.ConfiguredAudienceModelAssociation"
    """<p>Information about the configured audience model association that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredAudienceModelAssociationOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_audience_model_association

    out["configuredAudienceModelAssociation"] = (
        aws_sdk_cleanrooms.types.configured_audience_model_association.serialize_json(
            value["configured_audience_model_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetConfiguredAudienceModelAssociationOutput:
    out: GetConfiguredAudienceModelAssociationOutput = {}  # type: ignore[typeddict-item]
    if "configuredAudienceModelAssociation" in data:
        import aws_sdk_cleanrooms.types.configured_audience_model_association

        out["configured_audience_model_association"] = (
            aws_sdk_cleanrooms.types.configured_audience_model_association.deserialize_json(
                data["configuredAudienceModelAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelAssociationOutput.configured_audience_model_association required"
        )
    return out
