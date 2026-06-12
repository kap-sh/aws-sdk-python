"""Generated from Smithy shape ``com.amazonaws.lightsail#R53HostedZoneDeletionState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.r53_hosted_zone_deletion_state_code
    import aws_sdk_lightsail.types.string


class R53HostedZoneDeletionState(TypedDict):
    code: NotRequired[
        "aws_sdk_lightsail.types.r53_hosted_zone_deletion_state_code.R53HostedZoneDeletionStateCode"
    ]
    """<p>The status code for the deletion state.</p> <p>Following are the possible values:</p> <ul> <li> <p> <code>SUCCEEDED</code> - The hosted zone was successfully deleted.</p> </li> <li> <p> <code>PENDING</code> - The hosted zone deletion is in progress.</p> </li> <li> <p> <code>FAILED</code> - The hosted zone deletion failed.</p> </li> <li> <p> <code>STARTED</code> - The hosted zone deletion started.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The message that describes the reason for the status code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: R53HostedZoneDeletionState) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_lightsail.types.r53_hosted_zone_deletion_state_code

        out["code"] = (
            aws_sdk_lightsail.types.r53_hosted_zone_deletion_state_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> R53HostedZoneDeletionState:
    out: R53HostedZoneDeletionState = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_lightsail.types.r53_hosted_zone_deletion_state_code

        out["code"] = (
            aws_sdk_lightsail.types.r53_hosted_zone_deletion_state_code.deserialize_aws_json_1_1(
                data["code"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
