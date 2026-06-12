"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchEnableStandardsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_subscriptions


class BatchEnableStandardsResponse(TypedDict):
    standards_subscriptions: NotRequired[
        "aws_sdk_securityhub.types.standards_subscriptions.StandardsSubscriptions"
    ]
    """<p>The details of the standards subscriptions that were enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEnableStandardsResponse) -> dict:
    out: dict = {}
    if "standards_subscriptions" in value:
        import aws_sdk_securityhub.types.standards_subscriptions

        out["StandardsSubscriptions"] = (
            aws_sdk_securityhub.types.standards_subscriptions.serialize_json(
                value["standards_subscriptions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchEnableStandardsResponse:
    out: BatchEnableStandardsResponse = {}  # type: ignore[typeddict-item]
    if "StandardsSubscriptions" in data:
        import aws_sdk_securityhub.types.standards_subscriptions

        out["standards_subscriptions"] = (
            aws_sdk_securityhub.types.standards_subscriptions.deserialize_json(
                data["StandardsSubscriptions"]
            )
        )
    return out
