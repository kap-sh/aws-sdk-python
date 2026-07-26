"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListComponentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.component_summary_list
    import capo_ssm_sap.types.next_token


class ListComponentsOutput(TypedDict, closed=True):
    components: NotRequired[
        "capo_ssm_sap.types.component_summary_list.ComponentSummaryList"
    ]
    """<p>List of components registered with AWS System Manager for SAP.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsOutput) -> dict:
    out: dict = {}
    if "components" in value:
        import capo_ssm_sap.types.component_summary_list

        out["Components"] = capo_ssm_sap.types.component_summary_list.serialize_json(
            value["components"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsOutput:
    out: ListComponentsOutput = {}  # type: ignore[typeddict-item]
    if "Components" in data:
        import capo_ssm_sap.types.component_summary_list

        out["components"] = capo_ssm_sap.types.component_summary_list.deserialize_json(
            data["Components"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
