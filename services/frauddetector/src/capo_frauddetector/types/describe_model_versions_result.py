"""Generated from Smithy shape ``com.amazonaws.frauddetector#DescribeModelVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.model_version_detail_list
    import capo_frauddetector.types.string


class DescribeModelVersionsResult(TypedDict, closed=True):
    model_version_details: NotRequired[
        "capo_frauddetector.types.model_version_detail_list.modelVersionDetailList"
    ]
    """<p>The model version details.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelVersionsResult) -> dict:
    out: dict = {}
    if "model_version_details" in value:
        import capo_frauddetector.types.model_version_detail_list

        out["modelVersionDetails"] = (
            capo_frauddetector.types.model_version_detail_list.serialize_aws_json_1_1(
                value["model_version_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelVersionsResult:
    out: DescribeModelVersionsResult = {}  # type: ignore[typeddict-item]
    if "modelVersionDetails" in data:
        import capo_frauddetector.types.model_version_detail_list

        out["model_version_details"] = (
            capo_frauddetector.types.model_version_detail_list.deserialize_aws_json_1_1(
                data["modelVersionDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
