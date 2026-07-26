"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteRunsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.suite_run_information

SuiteRunsList: TypeAlias = list[
    "capo_iotdeviceadvisor.types.suite_run_information.SuiteRunInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuiteRunsList) -> list:
    import capo_iotdeviceadvisor.types.suite_run_information

    out: list = []
    for item in value:
        out.append(
            capo_iotdeviceadvisor.types.suite_run_information.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SuiteRunsList:
    import capo_iotdeviceadvisor.types.suite_run_information

    out: SuiteRunsList = []
    for item in data:
        out.append(
            capo_iotdeviceadvisor.types.suite_run_information.deserialize_json(item)
        )
    return out
