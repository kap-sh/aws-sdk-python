"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteRunConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.device_under_test
    import capo_iotdeviceadvisor.types.parallel_run
    import capo_iotdeviceadvisor.types.selected_test_list


class SuiteRunConfiguration(TypedDict, closed=True):
    primary_device: NotRequired[
        "capo_iotdeviceadvisor.types.device_under_test.DeviceUnderTest"
    ]
    """<p>Sets the primary device for the test suite run. This requires a thing ARN or a certificate ARN.</p>"""
    selected_test_list: NotRequired[
        "capo_iotdeviceadvisor.types.selected_test_list.SelectedTestList"
    ]
    """<p>Sets test case list.</p>"""
    parallel_run: NotRequired["capo_iotdeviceadvisor.types.parallel_run.ParallelRun"]
    """<p>TRUE if multiple test suites run in parallel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuiteRunConfiguration) -> dict:
    out: dict = {}
    if "primary_device" in value:
        import capo_iotdeviceadvisor.types.device_under_test

        out["primaryDevice"] = (
            capo_iotdeviceadvisor.types.device_under_test.serialize_json(
                value["primary_device"]
            )
        )
    if "selected_test_list" in value:
        import capo_iotdeviceadvisor.types.selected_test_list

        out["selectedTestList"] = (
            capo_iotdeviceadvisor.types.selected_test_list.serialize_json(
                value["selected_test_list"]
            )
        )
    if "parallel_run" in value:
        out["parallelRun"] = value["parallel_run"]
    return out


def deserialize_json(data: dict) -> SuiteRunConfiguration:
    out: SuiteRunConfiguration = {}  # type: ignore[typeddict-item]
    if "primaryDevice" in data:
        import capo_iotdeviceadvisor.types.device_under_test

        out["primary_device"] = (
            capo_iotdeviceadvisor.types.device_under_test.deserialize_json(
                data["primaryDevice"]
            )
        )
    if "selectedTestList" in data:
        import capo_iotdeviceadvisor.types.selected_test_list

        out["selected_test_list"] = (
            capo_iotdeviceadvisor.types.selected_test_list.deserialize_json(
                data["selectedTestList"]
            )
        )
    if "parallelRun" in data:
        out["parallel_run"] = data["parallelRun"]
    return out
