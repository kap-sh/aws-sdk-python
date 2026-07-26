"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#CreateSuiteDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.client_token
    import capo_iotdeviceadvisor.types.suite_definition_configuration
    import capo_iotdeviceadvisor.types.tag_map


class CreateSuiteDefinitionRequest(TypedDict, closed=True):
    suite_definition_configuration: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_configuration.SuiteDefinitionConfiguration"
    ]
    """<p>Creates a Device Advisor test suite with suite definition configuration.</p>"""
    tags: NotRequired["capo_iotdeviceadvisor.types.tag_map.TagMap"]
    """<p>The tags to be attached to the suite definition.</p>"""
    client_token: NotRequired["capo_iotdeviceadvisor.types.client_token.ClientToken"]
    """<p>The client token for the test suite definition creation. This token is used for tracking test suite definition creation using retries and obtaining its status. This parameter is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSuiteDefinitionRequest) -> dict:
    out: dict = {}
    if "suite_definition_configuration" in value:
        import capo_iotdeviceadvisor.types.suite_definition_configuration

        out["suiteDefinitionConfiguration"] = (
            capo_iotdeviceadvisor.types.suite_definition_configuration.serialize_json(
                value["suite_definition_configuration"]
            )
        )
    if "tags" in value:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSuiteDefinitionRequest:
    out: CreateSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionConfiguration" in data:
        import capo_iotdeviceadvisor.types.suite_definition_configuration

        out["suite_definition_configuration"] = (
            capo_iotdeviceadvisor.types.suite_definition_configuration.deserialize_json(
                data["suiteDefinitionConfiguration"]
            )
        )
    if "tags" in data:
        import capo_iotdeviceadvisor.types.tag_map

        out["tags"] = capo_iotdeviceadvisor.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
