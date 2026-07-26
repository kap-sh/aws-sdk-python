"""Generated from Smithy shape ``com.amazonaws.emr#ListStepsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_id
    import capo_emr.types.marker
    import capo_emr.types.step_state_list
    import capo_emr.types.xml_string_list


class ListStepsInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>The identifier of the cluster for which to list the steps.</p>"""
    step_states: NotRequired["capo_emr.types.step_state_list.StepStateList"]
    """<p>The filter to limit the step list based on certain states.</p>"""
    step_ids: NotRequired["capo_emr.types.xml_string_list.XmlStringList"]
    """<p>The filter to limit the step list based on the identifier of the steps. You can specify a maximum of ten Step IDs. The character constraint applies to the overall length of the array.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>The maximum number of steps that a single <code>ListSteps</code> action returns is 50. To return a longer list of steps, use multiple <code>ListSteps</code> actions along with the <code>Marker</code> parameter, which is a pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStepsInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "step_states" in value:
        import capo_emr.types.step_state_list

        out["StepStates"] = capo_emr.types.step_state_list.serialize_aws_json_1_1(
            value["step_states"]
        )
    if "step_ids" in value:
        import capo_emr.types.xml_string_list

        out["StepIds"] = capo_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["step_ids"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStepsInput:
    out: ListStepsInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "StepStates" in data:
        import capo_emr.types.step_state_list

        out["step_states"] = capo_emr.types.step_state_list.deserialize_aws_json_1_1(
            data["StepStates"]
        )
    if "StepIds" in data:
        import capo_emr.types.xml_string_list

        out["step_ids"] = capo_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["StepIds"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
