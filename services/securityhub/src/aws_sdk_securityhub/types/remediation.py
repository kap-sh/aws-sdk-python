"""Generated from Smithy shape ``com.amazonaws.securityhub#Remediation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.recommendation


class Remediation(TypedDict):
    recommendation: NotRequired[
        "aws_sdk_securityhub.types.recommendation.Recommendation"
    ]
    """<p>A recommendation on the steps to take to remediate the issue identified by a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Remediation) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import aws_sdk_securityhub.types.recommendation

        out["Recommendation"] = aws_sdk_securityhub.types.recommendation.serialize_json(
            value["recommendation"]
        )
    return out


def deserialize_json(data: dict) -> Remediation:
    out: Remediation = {}  # type: ignore[typeddict-item]
    if "Recommendation" in data:
        import aws_sdk_securityhub.types.recommendation

        out["recommendation"] = (
            aws_sdk_securityhub.types.recommendation.deserialize_json(
                data["Recommendation"]
            )
        )
    return out
