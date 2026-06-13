"""Generated from Smithy shape ``com.amazonaws.securitylake#GetSubscriberResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.subscriber_resource


class GetSubscriberResponse(TypedDict):
    subscriber: NotRequired[
        "aws_sdk_securitylake.types.subscriber_resource.SubscriberResource"
    ]
    """<p>The subscriber information for the specified subscriber ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriberResponse) -> dict:
    out: dict = {}
    if "subscriber" in value:
        import aws_sdk_securitylake.types.subscriber_resource

        out["subscriber"] = (
            aws_sdk_securitylake.types.subscriber_resource.serialize_json(
                value["subscriber"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSubscriberResponse:
    out: GetSubscriberResponse = {}  # type: ignore[typeddict-item]
    if "subscriber" in data:
        import aws_sdk_securitylake.types.subscriber_resource

        out["subscriber"] = (
            aws_sdk_securitylake.types.subscriber_resource.deserialize_json(
                data["subscriber"]
            )
        )
    return out
