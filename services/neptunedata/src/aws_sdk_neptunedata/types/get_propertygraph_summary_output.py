"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetPropertygraphSummaryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.propertygraph_summary_value_map


class GetPropertygraphSummaryOutput(TypedDict):
    status_code: NotRequired["int"]
    """<p>The HTTP return code of the request. If the request succeeded, the code is 200.</p>"""
    payload: NotRequired[
        "aws_sdk_neptunedata.types.propertygraph_summary_value_map.PropertygraphSummaryValueMap"
    ]
    """<p>Payload containing the property graph summary response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertygraphSummaryOutput) -> dict:
    out: dict = {}
    if "payload" in value:
        import aws_sdk_neptunedata.types.propertygraph_summary_value_map

        out["payload"] = (
            aws_sdk_neptunedata.types.propertygraph_summary_value_map.serialize_json(
                value["payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPropertygraphSummaryOutput:
    out: GetPropertygraphSummaryOutput = {}  # type: ignore[typeddict-item]
    if "payload" in data:
        import aws_sdk_neptunedata.types.propertygraph_summary_value_map

        out["payload"] = (
            aws_sdk_neptunedata.types.propertygraph_summary_value_map.deserialize_json(
                data["payload"]
            )
        )
    return out
