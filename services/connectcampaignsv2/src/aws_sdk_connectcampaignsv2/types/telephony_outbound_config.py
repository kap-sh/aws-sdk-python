"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TelephonyOutboundConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.answer_machine_detection_config
    import aws_sdk_connectcampaignsv2.types.contact_flow_id
    import aws_sdk_connectcampaignsv2.types.ring_timeout
    import aws_sdk_connectcampaignsv2.types.source_phone_number


class TelephonyOutboundConfig(TypedDict, closed=True):
    connect_contact_flow_id: (
        "aws_sdk_connectcampaignsv2.types.contact_flow_id.ContactFlowId"
    )
    connect_source_phone_number: NotRequired[
        "aws_sdk_connectcampaignsv2.types.source_phone_number.SourcePhoneNumber"
    ]
    answer_machine_detection_config: NotRequired[
        "aws_sdk_connectcampaignsv2.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
    ]
    ring_timeout: NotRequired[
        "aws_sdk_connectcampaignsv2.types.ring_timeout.RingTimeout"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyOutboundConfig) -> dict:
    out: dict = {}
    out["connectContactFlowId"] = value["connect_contact_flow_id"]
    if "connect_source_phone_number" in value:
        out["connectSourcePhoneNumber"] = value["connect_source_phone_number"]
    if "answer_machine_detection_config" in value:
        import aws_sdk_connectcampaignsv2.types.answer_machine_detection_config

        out["answerMachineDetectionConfig"] = (
            aws_sdk_connectcampaignsv2.types.answer_machine_detection_config.serialize_json(
                value["answer_machine_detection_config"]
            )
        )
    if "ring_timeout" in value:
        out["ringTimeout"] = value["ring_timeout"]
    return out


def deserialize_json(data: dict) -> TelephonyOutboundConfig:
    out: TelephonyOutboundConfig = {}  # type: ignore[typeddict-item]
    if "connectContactFlowId" in data:
        out["connect_contact_flow_id"] = data["connectContactFlowId"]
    else:
        raise DeserializationError(
            "TelephonyOutboundConfig.connect_contact_flow_id required"
        )
    if "connectSourcePhoneNumber" in data:
        out["connect_source_phone_number"] = data["connectSourcePhoneNumber"]
    if "answerMachineDetectionConfig" in data:
        import aws_sdk_connectcampaignsv2.types.answer_machine_detection_config

        out["answer_machine_detection_config"] = (
            aws_sdk_connectcampaignsv2.types.answer_machine_detection_config.deserialize_json(
                data["answerMachineDetectionConfig"]
            )
        )
    if "ringTimeout" in data:
        out["ring_timeout"] = data["ringTimeout"]
    return out
