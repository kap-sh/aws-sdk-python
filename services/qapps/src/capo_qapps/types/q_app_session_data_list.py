"""Generated from Smithy shape ``com.amazonaws.qapps#QAppSessionDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.q_app_session_data

QAppSessionDataList: TypeAlias = list[
    "capo_qapps.types.q_app_session_data.QAppSessionData"
]


# --- restJson1 ser/de ---
def serialize_json(value: QAppSessionDataList) -> list:
    import capo_qapps.types.q_app_session_data

    out: list = []
    for item in value:
        out.append(capo_qapps.types.q_app_session_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> QAppSessionDataList:
    import capo_qapps.types.q_app_session_data

    out: QAppSessionDataList = []
    for item in data:
        out.append(capo_qapps.types.q_app_session_data.deserialize_json(item))
    return out
