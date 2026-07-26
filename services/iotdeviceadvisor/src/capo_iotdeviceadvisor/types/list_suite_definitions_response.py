"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#ListSuiteDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.suite_definition_information_list
    import capo_iotdeviceadvisor.types.token


class ListSuiteDefinitionsResponse(TypedDict, closed=True):
    suite_definition_information_list: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_information_list.SuiteDefinitionInformationList"
    ]
    """<p>An array of objects that provide summaries of information about the suite definitions in the list.</p>"""
    next_token: NotRequired["capo_iotdeviceadvisor.types.token.Token"]
    """<p>A token used to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuiteDefinitionsResponse) -> dict:
    out: dict = {}
    if "suite_definition_information_list" in value:
        import capo_iotdeviceadvisor.types.suite_definition_information_list

        out["suiteDefinitionInformationList"] = (
            capo_iotdeviceadvisor.types.suite_definition_information_list.serialize_json(
                value["suite_definition_information_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSuiteDefinitionsResponse:
    out: ListSuiteDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionInformationList" in data:
        import capo_iotdeviceadvisor.types.suite_definition_information_list

        out["suite_definition_information_list"] = (
            capo_iotdeviceadvisor.types.suite_definition_information_list.deserialize_json(
                data["suiteDefinitionInformationList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
