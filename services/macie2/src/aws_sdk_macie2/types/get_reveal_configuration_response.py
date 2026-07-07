"""Generated from Smithy shape ``com.amazonaws.macie2#GetRevealConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.retrieval_configuration
    import aws_sdk_macie2.types.reveal_configuration


class GetRevealConfigurationResponse(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_macie2.types.reveal_configuration.RevealConfiguration"
    ]
    """<p>The KMS key that's used to encrypt the sensitive data, and the status of the configuration for the Amazon Macie account.</p>"""
    retrieval_configuration: NotRequired[
        "aws_sdk_macie2.types.retrieval_configuration.RetrievalConfiguration"
    ]
    """<p>The access method and settings that are used to retrieve the sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRevealConfigurationResponse) -> dict:
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


def deserialize_json(data: dict) -> GetRevealConfigurationResponse:
    out: GetRevealConfigurationResponse = {}  # type: ignore[typeddict-item]
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
