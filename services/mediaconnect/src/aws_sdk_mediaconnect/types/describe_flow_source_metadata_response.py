"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeFlowSourceMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediaconnect.types.__list_of_message_detail
    import aws_sdk_mediaconnect.types.ndi_source_metadata_info
    import aws_sdk_mediaconnect.types.transport_media_info


class DescribeFlowSourceMetadataResponse(TypedDict):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that DescribeFlowSourceMetadata was performed on.</p>"""
    messages: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p> Provides a status code and message regarding issues found with the flow source metadata.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp of the most recent change in metadata for this flow’s source.</p>"""
    transport_media_info: NotRequired[
        "aws_sdk_mediaconnect.types.transport_media_info.TransportMediaInfo"
    ]
    """<p> Information about the flow's transport media. </p>"""
    ndi_info: NotRequired[
        "aws_sdk_mediaconnect.types.ndi_source_metadata_info.NdiSourceMetadataInfo"
    ]
    """<p> The NDI® specific information about the flow's source. This includes the current active NDI sender, a list of all discovered NDI senders, the associated media streams for the active NDI sender, and any relevant status messages. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowSourceMetadataResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "messages" in value:
        import aws_sdk_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            aws_sdk_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["messages"]
            )
        )
    if "timestamp" in value:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["timestamp"] = aws_sdk_mediaconnect.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    if "transport_media_info" in value:
        import aws_sdk_mediaconnect.types.transport_media_info

        out["transportMediaInfo"] = (
            aws_sdk_mediaconnect.types.transport_media_info.serialize_json(
                value["transport_media_info"]
            )
        )
    if "ndi_info" in value:
        import aws_sdk_mediaconnect.types.ndi_source_metadata_info

        out["ndiInfo"] = (
            aws_sdk_mediaconnect.types.ndi_source_metadata_info.serialize_json(
                value["ndi_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeFlowSourceMetadataResponse:
    out: DescribeFlowSourceMetadataResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "messages" in data:
        import aws_sdk_mediaconnect.types.__list_of_message_detail

        out["messages"] = (
            aws_sdk_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["messages"]
            )
        )
    if "timestamp" in data:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    if "transportMediaInfo" in data:
        import aws_sdk_mediaconnect.types.transport_media_info

        out["transport_media_info"] = (
            aws_sdk_mediaconnect.types.transport_media_info.deserialize_json(
                data["transportMediaInfo"]
            )
        )
    if "ndiInfo" in data:
        import aws_sdk_mediaconnect.types.ndi_source_metadata_info

        out["ndi_info"] = (
            aws_sdk_mediaconnect.types.ndi_source_metadata_info.deserialize_json(
                data["ndiInfo"]
            )
        )
    return out
