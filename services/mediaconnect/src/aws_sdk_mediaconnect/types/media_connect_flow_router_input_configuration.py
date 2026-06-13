"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaConnectFlowRouterInputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn
    import aws_sdk_mediaconnect.types.flow_output_arn
    import aws_sdk_mediaconnect.types.flow_transit_encryption


class MediaConnectFlowRouterInputConfiguration(TypedDict):
    flow_arn: NotRequired["aws_sdk_mediaconnect.types.flow_arn.FlowArn"]
    """<p>The ARN of the flow to connect to.</p>"""
    flow_output_arn: NotRequired[
        "aws_sdk_mediaconnect.types.flow_output_arn.FlowOutputArn"
    ]
    """<p>The ARN of the flow output to connect to this router input.</p>"""
    source_transit_decryption: (
        "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
    )
    """<p>The decryption configuration for the flow source when connected to this router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectFlowRouterInputConfiguration) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_output_arn" in value:
        out["flowOutputArn"] = value["flow_output_arn"]
    import aws_sdk_mediaconnect.types.flow_transit_encryption

    out["sourceTransitDecryption"] = (
        aws_sdk_mediaconnect.types.flow_transit_encryption.serialize_json(
            value["source_transit_decryption"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaConnectFlowRouterInputConfiguration:
    out: MediaConnectFlowRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowOutputArn" in data:
        out["flow_output_arn"] = data["flowOutputArn"]
    if "sourceTransitDecryption" in data:
        import aws_sdk_mediaconnect.types.flow_transit_encryption

        out["source_transit_decryption"] = (
            aws_sdk_mediaconnect.types.flow_transit_encryption.deserialize_json(
                data["sourceTransitDecryption"]
            )
        )
    else:
        raise DeserializationError(
            "MediaConnectFlowRouterInputConfiguration.source_transit_decryption required"
        )
    return out
