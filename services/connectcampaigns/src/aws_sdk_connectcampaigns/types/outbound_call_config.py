"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#OutboundCallConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.answer_machine_detection_config
    import aws_sdk_connectcampaigns.types.contact_flow_id
    import aws_sdk_connectcampaigns.types.queue_id
    import aws_sdk_connectcampaigns.types.source_phone_number


class OutboundCallConfig(TypedDict, closed=True):
    connect_contact_flow_id: (
        "aws_sdk_connectcampaigns.types.contact_flow_id.ContactFlowId"
    )
    connect_source_phone_number: NotRequired[
        "aws_sdk_connectcampaigns.types.source_phone_number.SourcePhoneNumber"
    ]
    connect_queue_id: NotRequired["aws_sdk_connectcampaigns.types.queue_id.QueueId"]
    answer_machine_detection_config: NotRequired[
        "aws_sdk_connectcampaigns.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundCallConfig) -> dict:
    out: dict = {}
    out["connectContactFlowId"] = value["connect_contact_flow_id"]
    if "connect_source_phone_number" in value:
        out["connectSourcePhoneNumber"] = value["connect_source_phone_number"]
    if "connect_queue_id" in value:
        out["connectQueueId"] = value["connect_queue_id"]
    if "answer_machine_detection_config" in value:
        import aws_sdk_connectcampaigns.types.answer_machine_detection_config

        out["answerMachineDetectionConfig"] = (
            aws_sdk_connectcampaigns.types.answer_machine_detection_config.serialize_json(
                value["answer_machine_detection_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutboundCallConfig:
    out: OutboundCallConfig = {}  # type: ignore[typeddict-item]
    if "connectContactFlowId" in data:
        out["connect_contact_flow_id"] = data["connectContactFlowId"]
    else:
        raise DeserializationError(
            "OutboundCallConfig.connect_contact_flow_id required"
        )
    if "connectSourcePhoneNumber" in data:
        out["connect_source_phone_number"] = data["connectSourcePhoneNumber"]
    if "connectQueueId" in data:
        out["connect_queue_id"] = data["connectQueueId"]
    if "answerMachineDetectionConfig" in data:
        import aws_sdk_connectcampaigns.types.answer_machine_detection_config

        out["answer_machine_detection_config"] = (
            aws_sdk_connectcampaigns.types.answer_machine_detection_config.deserialize_json(
                data["answerMachineDetectionConfig"]
            )
        )
    return out
