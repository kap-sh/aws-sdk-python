"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WabaPhoneNumberSetupFinalizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.waba_phone_number_setup_finalization

WabaPhoneNumberSetupFinalizationList: TypeAlias = list[
    "capo_socialmessaging.types.waba_phone_number_setup_finalization.WabaPhoneNumberSetupFinalization"
]


# --- restJson1 ser/de ---
def serialize_json(value: WabaPhoneNumberSetupFinalizationList) -> list:
    import capo_socialmessaging.types.waba_phone_number_setup_finalization

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.waba_phone_number_setup_finalization.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WabaPhoneNumberSetupFinalizationList:
    import capo_socialmessaging.types.waba_phone_number_setup_finalization

    out: WabaPhoneNumberSetupFinalizationList = []
    for item in data:
        out.append(
            capo_socialmessaging.types.waba_phone_number_setup_finalization.deserialize_json(
                item
            )
        )
    return out
