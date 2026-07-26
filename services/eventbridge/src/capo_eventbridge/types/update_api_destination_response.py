"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateApiDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.api_destination_arn
    import capo_eventbridge.types.api_destination_state
    import capo_eventbridge.types.timestamp


class UpdateApiDestinationResponse(TypedDict, closed=True):
    api_destination_arn: NotRequired[
        "capo_eventbridge.types.api_destination_arn.ApiDestinationArn"
    ]
    """<p>The ARN of the API destination that was updated.</p>"""
    api_destination_state: NotRequired[
        "capo_eventbridge.types.api_destination_state.ApiDestinationState"
    ]
    """<p>The state of the API destination that was updated.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the API destination was created.</p>"""
    last_modified_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the API destination was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApiDestinationResponse) -> dict:
    out: dict = {}
    if "api_destination_arn" in value:
        out["ApiDestinationArn"] = value["api_destination_arn"]
    if "api_destination_state" in value:
        import capo_eventbridge.types.api_destination_state

        out["ApiDestinationState"] = (
            capo_eventbridge.types.api_destination_state.serialize_aws_json_1_1(
                value["api_destination_state"]
            )
        )
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApiDestinationResponse:
    out: UpdateApiDestinationResponse = {}  # type: ignore[typeddict-item]
    if "ApiDestinationArn" in data:
        out["api_destination_arn"] = data["ApiDestinationArn"]
    if "ApiDestinationState" in data:
        import capo_eventbridge.types.api_destination_state

        out["api_destination_state"] = (
            capo_eventbridge.types.api_destination_state.deserialize_aws_json_1_1(
                data["ApiDestinationState"]
            )
        )
    if "CreationTime" in data:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_eventbridge.types.timestamp

        out["last_modified_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
