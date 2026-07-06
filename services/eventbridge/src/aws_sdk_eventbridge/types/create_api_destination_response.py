"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateApiDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.api_destination_arn
    import aws_sdk_eventbridge.types.api_destination_state
    import aws_sdk_eventbridge.types.timestamp


class CreateApiDestinationResponse(TypedDict, closed=True):
    api_destination_arn: NotRequired[
        "aws_sdk_eventbridge.types.api_destination_arn.ApiDestinationArn"
    ]
    """<p>The ARN of the API destination that was created by the request.</p>"""
    api_destination_state: NotRequired[
        "aws_sdk_eventbridge.types.api_destination_state.ApiDestinationState"
    ]
    """<p>The state of the API destination that was created by the request.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp indicating the time that the API destination was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp indicating the time that the API destination was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApiDestinationResponse) -> dict:
    out: dict = {}
    if "api_destination_arn" in value:
        out["ApiDestinationArn"] = value["api_destination_arn"]
    if "api_destination_state" in value:
        import aws_sdk_eventbridge.types.api_destination_state

        out["ApiDestinationState"] = (
            aws_sdk_eventbridge.types.api_destination_state.serialize_aws_json_1_1(
                value["api_destination_state"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApiDestinationResponse:
    out: CreateApiDestinationResponse = {}  # type: ignore[typeddict-item]
    if "ApiDestinationArn" in data:
        out["api_destination_arn"] = data["ApiDestinationArn"]
    if "ApiDestinationState" in data:
        import aws_sdk_eventbridge.types.api_destination_state

        out["api_destination_state"] = (
            aws_sdk_eventbridge.types.api_destination_state.deserialize_aws_json_1_1(
                data["ApiDestinationState"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
