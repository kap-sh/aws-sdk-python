"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateRevealConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.retrieval_configuration
    import aws_sdk_macie2.types.reveal_configuration


class UpdateRevealConfigurationResponse(TypedDict):
    configuration: NotRequired[
        "aws_sdk_macie2.types.reveal_configuration.RevealConfiguration"
    ]
    """<p>The KMS key to use to encrypt the sensitive data, and the status of the configuration for the Amazon Macie account.</p>"""
    retrieval_configuration: NotRequired[
        "aws_sdk_macie2.types.retrieval_configuration.RetrievalConfiguration"
    ]
    """<p>The access method and settings to use when retrieving the sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRevealConfigurationResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_macie2.types.reveal_configuration

        out["configuration"] = aws_sdk_macie2.types.reveal_configuration.serialize_json(
            value["configuration"]
        )
    if "retrieval_configuration" in value:
        import aws_sdk_macie2.types.retrieval_configuration

        out["retrievalConfiguration"] = (
            aws_sdk_macie2.types.retrieval_configuration.serialize_json(
                value["retrieval_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRevealConfigurationResponse:
    out: UpdateRevealConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_macie2.types.reveal_configuration

        out["configuration"] = (
            aws_sdk_macie2.types.reveal_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "retrievalConfiguration" in data:
        import aws_sdk_macie2.types.retrieval_configuration

        out["retrieval_configuration"] = (
            aws_sdk_macie2.types.retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    return out
