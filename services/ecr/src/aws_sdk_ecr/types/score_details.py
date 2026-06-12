"""Generated from Smithy shape ``com.amazonaws.ecr#ScoreDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.cvss_score_details


class ScoreDetails(TypedDict):
    cvss: NotRequired["aws_sdk_ecr.types.cvss_score_details.CvssScoreDetails"]
    """<p>An object that contains details about the CVSS score given to a finding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScoreDetails) -> dict:
    out: dict = {}
    if "cvss" in value:
        import aws_sdk_ecr.types.cvss_score_details

        out["cvss"] = aws_sdk_ecr.types.cvss_score_details.serialize_aws_json_1_1(
            value["cvss"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScoreDetails:
    out: ScoreDetails = {}  # type: ignore[typeddict-item]
    if "cvss" in data:
        import aws_sdk_ecr.types.cvss_score_details

        out["cvss"] = aws_sdk_ecr.types.cvss_score_details.deserialize_aws_json_1_1(
            data["cvss"]
        )
    return out
