"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaUngraceful``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.lambda_ungraceful_behavior


class LambdaUngraceful(TypedDict):
    behavior: "aws_sdk_arc_region_switch.types.lambda_ungraceful_behavior.LambdaUngracefulBehavior"
    """<p>The ungraceful behavior for a Lambda function, which must be set to <code>skip</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaUngraceful) -> dict:
    out: dict = {}
    import aws_sdk_arc_region_switch.types.lambda_ungraceful_behavior

    out["behavior"] = (
        aws_sdk_arc_region_switch.types.lambda_ungraceful_behavior.serialize_aws_json_1_0(
            value.get("behavior", "skip")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaUngraceful:
    out: LambdaUngraceful = {}  # type: ignore[typeddict-item]
    if "behavior" in data:
        import aws_sdk_arc_region_switch.types.lambda_ungraceful_behavior

        out["behavior"] = (
            aws_sdk_arc_region_switch.types.lambda_ungraceful_behavior.deserialize_aws_json_1_0(
                data["behavior"]
            )
        )
    else:
        out["behavior"] = "skip"
    return out
