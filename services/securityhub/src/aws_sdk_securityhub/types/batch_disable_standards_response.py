"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchDisableStandardsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_subscriptions


class BatchDisableStandardsResponse(TypedDict, closed=True):
    standards_subscriptions: NotRequired[
        "aws_sdk_securityhub.types.standards_subscriptions.StandardsSubscriptions"
    ]
    """<p>The details of the standards subscriptions that were disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisableStandardsResponse) -> dict:
    out: dict = {}
    if "standards_subscriptions" in value:
        import aws_sdk_securityhub.types.standards_subscriptions

        out["StandardsSubscriptions"] = (
            aws_sdk_securityhub.types.standards_subscriptions.serialize_json(
                value["standards_subscriptions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDisableStandardsResponse:
    out: BatchDisableStandardsResponse = {}  # type: ignore[typeddict-item]
    if "StandardsSubscriptions" in data:
        import aws_sdk_securityhub.types.standards_subscriptions

        out["standards_subscriptions"] = (
            aws_sdk_securityhub.types.standards_subscriptions.deserialize_json(
                data["StandardsSubscriptions"]
            )
        )
    return out
