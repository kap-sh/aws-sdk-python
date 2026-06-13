"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EventSourceMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.event_source_mapping_arn
    import aws_sdk_arc_region_switch.types.iam_role_arn


class EventSourceMapping(TypedDict):
    cross_account_role: NotRequired[
        "aws_sdk_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    arn: (
        "aws_sdk_arc_region_switch.types.event_source_mapping_arn.EventSourceMappingArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Lambda event source mapping.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventSourceMapping) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EventSourceMapping:
    out: EventSourceMapping = {}  # type: ignore[typeddict-item]
    if "crossAccountRole" in data:
        out["cross_account_role"] = data["crossAccountRole"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EventSourceMapping.arn required")
    return out
