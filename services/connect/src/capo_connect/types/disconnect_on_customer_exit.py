"""Generated from Smithy shape ``com.amazonaws.connect#DisconnectOnCustomerExit``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.disconnect_on_customer_exit_participant_type

DisconnectOnCustomerExit: TypeAlias = list[
    "capo_connect.types.disconnect_on_customer_exit_participant_type.DisconnectOnCustomerExitParticipantType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectOnCustomerExit) -> list:
    import capo_connect.types.disconnect_on_customer_exit_participant_type

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.disconnect_on_customer_exit_participant_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DisconnectOnCustomerExit:
    import capo_connect.types.disconnect_on_customer_exit_participant_type

    out: DisconnectOnCustomerExit = []
    for item in data:
        out.append(
            capo_connect.types.disconnect_on_customer_exit_participant_type.deserialize_json(
                item
            )
        )
    return out
