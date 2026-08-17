"""Generated from Smithy shape ``com.amazonaws.ecr#ScoreDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.cvss_score_details


class ScoreDetails(TypedDict, closed=True):
    cvss: NotRequired["capo_ecr.types.cvss_score_details.CvssScoreDetails"]
    """<p>An object that contains details about the CVSS score given to a finding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScoreDetails) -> dict:
    out: dict = {}
    if "cvss" in value:
        import capo_ecr.types.cvss_score_details

        out["cvss"] = capo_ecr.types.cvss_score_details.serialize_aws_json_1_1(
            value["cvss"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScoreDetails:
    out: ScoreDetails = {}  # type: ignore[typeddict-item]
    if data.get("cvss") is not None:
        import capo_ecr.types.cvss_score_details

        out["cvss"] = capo_ecr.types.cvss_score_details.deserialize_aws_json_1_1(
            data["cvss"]
        )
    return out
