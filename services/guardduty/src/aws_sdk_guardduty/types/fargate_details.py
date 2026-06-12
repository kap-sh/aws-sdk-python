"""Generated from Smithy shape ``com.amazonaws.guardduty#FargateDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.issues
    import aws_sdk_guardduty.types.management_type


class FargateDetails(TypedDict):
    issues: NotRequired["aws_sdk_guardduty.types.issues.Issues"]
    """<p>Runtime coverage issues identified for the resource running on Amazon Web Services Fargate.</p>"""
    management_type: NotRequired[
        "aws_sdk_guardduty.types.management_type.ManagementType"
    ]
    """<p>Indicates how the GuardDuty security agent is managed for this resource.</p> <ul> <li> <p> <code>AUTO_MANAGED</code> indicates that GuardDuty deploys and manages updates for this resource.</p> </li> <li> <p> <code>DISABLED</code> indicates that the deployment of the GuardDuty security agent is disabled for this resource.</p> </li> </ul> <note> <p>The <code>MANUAL</code> status doesn't apply to the Amazon Web Services Fargate (Amazon ECS only) woprkloads.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: FargateDetails) -> dict:
    out: dict = {}
    if "issues" in value:
        import aws_sdk_guardduty.types.issues

        out["issues"] = aws_sdk_guardduty.types.issues.serialize_json(value["issues"])
    if "management_type" in value:
        import aws_sdk_guardduty.types.management_type

        out["managementType"] = aws_sdk_guardduty.types.management_type.serialize_json(
            value["management_type"]
        )
    return out


def deserialize_json(data: dict) -> FargateDetails:
    out: FargateDetails = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import aws_sdk_guardduty.types.issues

        out["issues"] = aws_sdk_guardduty.types.issues.deserialize_json(data["issues"])
    if "managementType" in data:
        import aws_sdk_guardduty.types.management_type

        out["management_type"] = (
            aws_sdk_guardduty.types.management_type.deserialize_json(
                data["managementType"]
            )
        )
    return out
