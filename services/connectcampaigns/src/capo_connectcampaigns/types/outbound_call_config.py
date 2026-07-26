"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#OutboundCallConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaigns.types.answer_machine_detection_config
    import capo_connectcampaigns.types.contact_flow_id
    import capo_connectcampaigns.types.queue_id
    import capo_connectcampaigns.types.source_phone_number


class OutboundCallConfig(TypedDict, closed=True):
    connect_contact_flow_id: "capo_connectcampaigns.types.contact_flow_id.ContactFlowId"
    connect_source_phone_number: NotRequired[
        "capo_connectcampaigns.types.source_phone_number.SourcePhoneNumber"
    ]
    connect_queue_id: NotRequired["capo_connectcampaigns.types.queue_id.QueueId"]
    answer_machine_detection_config: NotRequired[
        "capo_connectcampaigns.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
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
        import capo_connectcampaigns.types.answer_machine_detection_config

        out["answerMachineDetectionConfig"] = (
            capo_connectcampaigns.types.answer_machine_detection_config.serialize_json(
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
        import capo_connectcampaigns.types.answer_machine_detection_config

        out["answer_machine_detection_config"] = (
            capo_connectcampaigns.types.answer_machine_detection_config.deserialize_json(
                data["answerMachineDetectionConfig"]
            )
        )
    return out
