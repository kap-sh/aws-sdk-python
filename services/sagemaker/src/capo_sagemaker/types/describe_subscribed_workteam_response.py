"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeSubscribedWorkteamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.subscribed_workteam


class DescribeSubscribedWorkteamResponse(TypedDict, closed=True):
    subscribed_workteam: NotRequired[
        "capo_sagemaker.types.subscribed_workteam.SubscribedWorkteam"
    ]
    """<p>A <code>Workteam</code> instance that contains information about the work team.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscribedWorkteamResponse) -> dict:
    out: dict = {}
    if "subscribed_workteam" in value:
        import capo_sagemaker.types.subscribed_workteam

        out["SubscribedWorkteam"] = (
            capo_sagemaker.types.subscribed_workteam.serialize_aws_json_1_1(
                value["subscribed_workteam"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscribedWorkteamResponse:
    out: DescribeSubscribedWorkteamResponse = {}  # type: ignore[typeddict-item]
    if "SubscribedWorkteam" in data:
        import capo_sagemaker.types.subscribed_workteam

        out["subscribed_workteam"] = (
            capo_sagemaker.types.subscribed_workteam.deserialize_aws_json_1_1(
                data["SubscribedWorkteam"]
            )
        )
    return out
