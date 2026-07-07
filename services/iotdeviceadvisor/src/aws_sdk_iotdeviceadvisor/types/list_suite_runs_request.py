"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#ListSuiteRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.max_results
    import aws_sdk_iotdeviceadvisor.types.suite_definition_version
    import aws_sdk_iotdeviceadvisor.types.token
    import aws_sdk_iotdeviceadvisor.types.uuid


class ListSuiteRunsRequest(TypedDict, closed=True):
    suite_definition_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Lists the test suite runs of the specified test suite based on suite definition ID.</p>"""
    suite_definition_version: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Must be passed along with <code>suiteDefinitionId</code>. Lists the test suite runs of the specified test suite based on suite definition version.</p>"""
    max_results: NotRequired["aws_sdk_iotdeviceadvisor.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at once.</p>"""
    next_token: NotRequired["aws_sdk_iotdeviceadvisor.types.token.Token"]
    """<p>A token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuiteRunsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSuiteRunsRequest:
    out: ListSuiteRunsRequest = {}  # type: ignore[typeddict-item]
    return out
