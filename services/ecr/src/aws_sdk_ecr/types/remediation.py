"""Generated from Smithy shape ``com.amazonaws.ecr#Remediation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.recommendation


class Remediation(TypedDict, closed=True):
    recommendation: NotRequired["aws_sdk_ecr.types.recommendation.Recommendation"]
    """<p>An object that contains information about the recommended course of action to remediate the finding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Remediation) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import aws_sdk_ecr.types.recommendation

        out["recommendation"] = aws_sdk_ecr.types.recommendation.serialize_aws_json_1_1(
            value["recommendation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Remediation:
    out: Remediation = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import aws_sdk_ecr.types.recommendation

        out["recommendation"] = (
            aws_sdk_ecr.types.recommendation.deserialize_aws_json_1_1(
                data["recommendation"]
            )
        )
    return out
