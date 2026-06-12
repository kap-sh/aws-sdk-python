"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#DescribeScalableTargetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.scalable_targets
    import aws_sdk_application_auto_scaling.types.xml_string


class DescribeScalableTargetsResponse(TypedDict):
    scalable_targets: NotRequired[
        "aws_sdk_application_auto_scaling.types.scalable_targets.ScalableTargets"
    ]
    """<p>The scalable targets that match the request parameters.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_auto_scaling.types.xml_string.XmlString"
    ]
    """<p>The token required to get the next set of results. This value is <code>null</code> if there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalableTargetsResponse) -> dict:
    out: dict = {}
    if "scalable_targets" in value:
        import aws_sdk_application_auto_scaling.types.scalable_targets

        out["ScalableTargets"] = (
            aws_sdk_application_auto_scaling.types.scalable_targets.serialize_aws_json_1_1(
                value["scalable_targets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalableTargetsResponse:
    out: DescribeScalableTargetsResponse = {}  # type: ignore[typeddict-item]
    if "ScalableTargets" in data:
        import aws_sdk_application_auto_scaling.types.scalable_targets

        out["scalable_targets"] = (
            aws_sdk_application_auto_scaling.types.scalable_targets.deserialize_aws_json_1_1(
                data["ScalableTargets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
