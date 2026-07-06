"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PreviewPrivacyImpactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.privacy_impact


class PreviewPrivacyImpactOutput(TypedDict, closed=True):
    privacy_impact: "aws_sdk_cleanrooms.types.privacy_impact.PrivacyImpact"
    """<p>An estimate of the number of aggregation functions that the member who can query can run given the epsilon and noise parameters. This does not change the privacy budget.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreviewPrivacyImpactOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.privacy_impact

    out["privacyImpact"] = aws_sdk_cleanrooms.types.privacy_impact.serialize_json(
        value["privacy_impact"]
    )
    return out


def deserialize_json(data: dict) -> PreviewPrivacyImpactOutput:
    out: PreviewPrivacyImpactOutput = {}  # type: ignore[typeddict-item]
    if "privacyImpact" in data:
        import aws_sdk_cleanrooms.types.privacy_impact

        out["privacy_impact"] = (
            aws_sdk_cleanrooms.types.privacy_impact.deserialize_json(
                data["privacyImpact"]
            )
        )
    else:
        raise DeserializationError("PreviewPrivacyImpactOutput.privacy_impact required")
    return out
