"""Generated from Smithy shape ``com.amazonaws.medialive#Smpte2110ReceiverGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_smpte2110_receiver_group


class Smpte2110ReceiverGroupSettings(TypedDict):
    smpte2110_receiver_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of_smpte2110_receiver_group.__listOfSmpte2110ReceiverGroup"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Smpte2110ReceiverGroupSettings) -> dict:
    out: dict = {}
    if "smpte2110_receiver_groups" in value:
        import aws_sdk_medialive.types.__list_of_smpte2110_receiver_group

        out["smpte2110ReceiverGroups"] = (
            aws_sdk_medialive.types.__list_of_smpte2110_receiver_group.serialize_json(
                value["smpte2110_receiver_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> Smpte2110ReceiverGroupSettings:
    out: Smpte2110ReceiverGroupSettings = {}  # type: ignore[typeddict-item]
    if "smpte2110ReceiverGroups" in data:
        import aws_sdk_medialive.types.__list_of_smpte2110_receiver_group

        out["smpte2110_receiver_groups"] = (
            aws_sdk_medialive.types.__list_of_smpte2110_receiver_group.deserialize_json(
                data["smpte2110ReceiverGroups"]
            )
        )
    return out
