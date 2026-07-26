"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateSubscriberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.subscriber_resource


class CreateSubscriberResponse(TypedDict, closed=True):
    subscriber: NotRequired[
        "capo_securitylake.types.subscriber_resource.SubscriberResource"
    ]
    """<p>Retrieve information about the subscriber created using the <code>CreateSubscriber</code> API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriberResponse) -> dict:
    out: dict = {}
    if "subscriber" in value:
        import capo_securitylake.types.subscriber_resource

        out["subscriber"] = capo_securitylake.types.subscriber_resource.serialize_json(
            value["subscriber"]
        )
    return out


def deserialize_json(data: dict) -> CreateSubscriberResponse:
    out: CreateSubscriberResponse = {}  # type: ignore[typeddict-item]
    if "subscriber" in data:
        import capo_securitylake.types.subscriber_resource

        out["subscriber"] = (
            capo_securitylake.types.subscriber_resource.deserialize_json(
                data["subscriber"]
            )
        )
    return out
