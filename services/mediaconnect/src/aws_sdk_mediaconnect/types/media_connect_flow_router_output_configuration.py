"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaConnectFlowRouterOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn
    import aws_sdk_mediaconnect.types.flow_source_arn
    import aws_sdk_mediaconnect.types.flow_transit_encryption


class MediaConnectFlowRouterOutputConfiguration(TypedDict):
    flow_arn: NotRequired["aws_sdk_mediaconnect.types.flow_arn.FlowArn"]
    """<p>The ARN of the flow to connect to this router output.</p>"""
    flow_source_arn: NotRequired[
        "aws_sdk_mediaconnect.types.flow_source_arn.FlowSourceArn"
    ]
    """<p>The ARN of the flow source to connect to this router output.</p>"""
    destination_transit_encryption: (
        "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
    )
    """<p>The encryption configuration for the flow destination when connected to this router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectFlowRouterOutputConfiguration) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_source_arn" in value:
        out["flowSourceArn"] = value["flow_source_arn"]
    import aws_sdk_mediaconnect.types.flow_transit_encryption

    out["destinationTransitEncryption"] = (
        aws_sdk_mediaconnect.types.flow_transit_encryption.serialize_json(
            value["destination_transit_encryption"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaConnectFlowRouterOutputConfiguration:
    out: MediaConnectFlowRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowSourceArn" in data:
        out["flow_source_arn"] = data["flowSourceArn"]
    if "destinationTransitEncryption" in data:
        import aws_sdk_mediaconnect.types.flow_transit_encryption

        out["destination_transit_encryption"] = (
            aws_sdk_mediaconnect.types.flow_transit_encryption.deserialize_json(
                data["destinationTransitEncryption"]
            )
        )
    else:
        raise DeserializationError(
            "MediaConnectFlowRouterOutputConfiguration.destination_transit_encryption required"
        )
    return out
