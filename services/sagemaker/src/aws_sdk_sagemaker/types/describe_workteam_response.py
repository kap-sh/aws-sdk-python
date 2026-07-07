"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeWorkteamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workteam


class DescribeWorkteamResponse(TypedDict, closed=True):
    workteam: NotRequired["aws_sdk_sagemaker.types.workteam.Workteam"]
    """<p>A <code>Workteam</code> instance that contains information about the work team. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkteamResponse) -> dict:
    out: dict = {}
    if "workteam" in value:
        import aws_sdk_sagemaker.types.workteam

        out["Workteam"] = aws_sdk_sagemaker.types.workteam.serialize_aws_json_1_1(
            value["workteam"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkteamResponse:
    out: DescribeWorkteamResponse = {}  # type: ignore[typeddict-item]
    if "Workteam" in data:
        import aws_sdk_sagemaker.types.workteam

        out["workteam"] = aws_sdk_sagemaker.types.workteam.deserialize_aws_json_1_1(
            data["Workteam"]
        )
    return out
