"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#StartSuiteRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.suite_definition_version
    import capo_iotdeviceadvisor.types.suite_run_configuration
    import capo_iotdeviceadvisor.types.tag_map
    import capo_iotdeviceadvisor.types.uuid


class StartSuiteRunRequest(TypedDict, closed=True):
    suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite definition ID of the test suite.</p>"""
    suite_definition_version: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Suite definition version of the test suite.</p>"""
    suite_run_configuration: NotRequired[
        "capo_iotdeviceadvisor.types.suite_run_configuration.SuiteRunConfiguration"
    ]
    """<p>Suite run configuration.</p>"""
    tags: NotRequired["capo_iotdeviceadvisor.types.tag_map.TagMap"]
    """<p>The tags to be attached to the suite run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSuiteRunRequest) -> dict:
    out: dict = {}
    if "suite_definition_version" in value:
        out["suiteDefinitionVersion"] = value["suite_definition_version"]
    if "suite_run_configuration" in value:
        import capo_iotdeviceadvisor.types.suite_run_configuration

        out["suiteRunConfiguration"] = (
            capo_iotdeviceadvisor.types.suite_run_configuration.serialize_json(
                value["suite_run_configuration"]
            )
        )
    if "tags" in value:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartSuiteRunRequest:
    out: StartSuiteRunRequest = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionVersion" in data:
        out["suite_definition_version"] = data["suiteDefinitionVersion"]
    if "suiteRunConfiguration" in data:
        import capo_iotdeviceadvisor.types.suite_run_configuration

        out["suite_run_configuration"] = (
            capo_iotdeviceadvisor.types.suite_run_configuration.deserialize_json(
                data["suiteRunConfiguration"]
            )
        )
    if "tags" in data:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.deserialize_json(data["tags"])
    return out
