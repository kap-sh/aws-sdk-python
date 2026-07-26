"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TelephonyChannelSubtypeParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.answer_machine_detection_config
    import capo_connectcampaignsv2.types.attributes
    import capo_connectcampaignsv2.types.destination_phone_number
    import capo_connectcampaignsv2.types.ring_timeout
    import capo_connectcampaignsv2.types.source_phone_number


class TelephonyChannelSubtypeParameters(TypedDict, closed=True):
    destination_phone_number: (
        "capo_connectcampaignsv2.types.destination_phone_number.DestinationPhoneNumber"
    )
    attributes: "capo_connectcampaignsv2.types.attributes.Attributes"
    connect_source_phone_number: NotRequired[
        "capo_connectcampaignsv2.types.source_phone_number.SourcePhoneNumber"
    ]
    answer_machine_detection_config: NotRequired[
        "capo_connectcampaignsv2.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
    ]
    ring_timeout: NotRequired["capo_connectcampaignsv2.types.ring_timeout.RingTimeout"]


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyChannelSubtypeParameters) -> dict:
    out: dict = {}
    out["destinationPhoneNumber"] = value["destination_phone_number"]
    import capo_connectcampaignsv2.types.attributes

    out["attributes"] = capo_connectcampaignsv2.types.attributes.serialize_json(
        value["attributes"]
    )
    if "connect_source_phone_number" in value:
        out["connectSourcePhoneNumber"] = value["connect_source_phone_number"]
    if "answer_machine_detection_config" in value:
        import capo_connectcampaignsv2.types.answer_machine_detection_config

        out["answerMachineDetectionConfig"] = (
            capo_connectcampaignsv2.types.answer_machine_detection_config.serialize_json(
                value["answer_machine_detection_config"]
            )
        )
    if "ring_timeout" in value:
        out["ringTimeout"] = value["ring_timeout"]
    return out


def deserialize_json(data: dict) -> TelephonyChannelSubtypeParameters:
    out: TelephonyChannelSubtypeParameters = {}  # type: ignore[typeddict-item]
    if "destinationPhoneNumber" in data:
        out["destination_phone_number"] = data["destinationPhoneNumber"]
    else:
        raise DeserializationError(
            "TelephonyChannelSubtypeParameters.destination_phone_number required"
        )
    if "attributes" in data:
        import capo_connectcampaignsv2.types.attributes

        out["attributes"] = capo_connectcampaignsv2.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        raise DeserializationError(
            "TelephonyChannelSubtypeParameters.attributes required"
        )
    if "connectSourcePhoneNumber" in data:
        out["connect_source_phone_number"] = data["connectSourcePhoneNumber"]
    if "answerMachineDetectionConfig" in data:
        import capo_connectcampaignsv2.types.answer_machine_detection_config

        out["answer_machine_detection_config"] = (
            capo_connectcampaignsv2.types.answer_machine_detection_config.deserialize_json(
                data["answerMachineDetectionConfig"]
            )
        )
    if "ringTimeout" in data:
        out["ring_timeout"] = data["ringTimeout"]
    return out
