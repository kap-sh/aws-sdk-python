"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#UpdateCampaignOutboundCallConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.answer_machine_detection_config
    import aws_sdk_connectcampaigns.types.campaign_id
    import aws_sdk_connectcampaigns.types.contact_flow_id
    import aws_sdk_connectcampaigns.types.source_phone_number


class UpdateCampaignOutboundCallConfigRequest(TypedDict, closed=True):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"
    connect_contact_flow_id: NotRequired[
        "aws_sdk_connectcampaigns.types.contact_flow_id.ContactFlowId"
    ]
    connect_source_phone_number: NotRequired[
        "aws_sdk_connectcampaigns.types.source_phone_number.SourcePhoneNumber"
    ]
    answer_machine_detection_config: NotRequired[
        "aws_sdk_connectcampaigns.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignOutboundCallConfigRequest) -> dict:
    out: dict = {}
    if "connect_contact_flow_id" in value:
        out["connectContactFlowId"] = value["connect_contact_flow_id"]
    if "connect_source_phone_number" in value:
        out["connectSourcePhoneNumber"] = value["connect_source_phone_number"]
    if "answer_machine_detection_config" in value:
        import aws_sdk_connectcampaigns.types.answer_machine_detection_config

        out["answerMachineDetectionConfig"] = (
            aws_sdk_connectcampaigns.types.answer_machine_detection_config.serialize_json(
                value["answer_machine_detection_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCampaignOutboundCallConfigRequest:
    out: UpdateCampaignOutboundCallConfigRequest = {}  # type: ignore[typeddict-item]
    if "connectContactFlowId" in data:
        out["connect_contact_flow_id"] = data["connectContactFlowId"]
    if "connectSourcePhoneNumber" in data:
        out["connect_source_phone_number"] = data["connectSourcePhoneNumber"]
    if "answerMachineDetectionConfig" in data:
        import aws_sdk_connectcampaigns.types.answer_machine_detection_config

        out["answer_machine_detection_config"] = (
            aws_sdk_connectcampaigns.types.answer_machine_detection_config.deserialize_json(
                data["answerMachineDetectionConfig"]
            )
        )
    return out
