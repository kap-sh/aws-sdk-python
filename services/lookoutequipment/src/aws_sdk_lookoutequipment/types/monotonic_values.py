"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#MonotonicValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.monotonicity
    import aws_sdk_lookoutequipment.types.statistical_issue_status


class MonotonicValues(TypedDict):
    status: (
        "aws_sdk_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to having monotonic values. </p>"""
    monotonicity: NotRequired[
        "aws_sdk_lookoutequipment.types.monotonicity.Monotonicity"
    ]
    """<p> Indicates the monotonicity of values. Can be INCREASING, DECREASING, or STATIC. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonotonicValues) -> dict:
    out: dict = {}
    import aws_sdk_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        aws_sdk_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "monotonicity" in value:
        import aws_sdk_lookoutequipment.types.monotonicity

        out["Monotonicity"] = (
            aws_sdk_lookoutequipment.types.monotonicity.serialize_aws_json_1_0(
                value["monotonicity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonotonicValues:
    out: MonotonicValues = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.statistical_issue_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.statistical_issue_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("MonotonicValues.status required")
    if "Monotonicity" in data:
        import aws_sdk_lookoutequipment.types.monotonicity

        out["monotonicity"] = (
            aws_sdk_lookoutequipment.types.monotonicity.deserialize_aws_json_1_0(
                data["Monotonicity"]
            )
        )
    return out
