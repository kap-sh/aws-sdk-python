"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#StartHumanLoopRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_a2i_runtime.types.flow_definition_arn
    import capo_sagemaker_a2i_runtime.types.human_loop_data_attributes
    import capo_sagemaker_a2i_runtime.types.human_loop_input
    import capo_sagemaker_a2i_runtime.types.human_loop_name


class StartHumanLoopRequest(TypedDict, closed=True):
    human_loop_name: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
    ]
    """<p>The name of the human loop.</p>"""
    flow_definition_arn: NotRequired[
        "capo_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flow definition associated with this human loop.</p>"""
    human_loop_input: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_input.HumanLoopInput"
    ]
    """<p>An object that contains information about the human loop.</p>"""
    data_attributes: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_data_attributes.HumanLoopDataAttributes"
    ]
    """<p>Attributes of the specified data. Use <code>DataAttributes</code> to specify if your data is free of personally identifiable information and/or free of adult content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartHumanLoopRequest) -> dict:
    out: dict = {}
    if "human_loop_name" in value:
        out["HumanLoopName"] = value["human_loop_name"]
    if "flow_definition_arn" in value:
        out["FlowDefinitionArn"] = value["flow_definition_arn"]
    if "human_loop_input" in value:
        import capo_sagemaker_a2i_runtime.types.human_loop_input

        out["HumanLoopInput"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_input.serialize_json(
                value["human_loop_input"]
            )
        )
    if "data_attributes" in value:
        import capo_sagemaker_a2i_runtime.types.human_loop_data_attributes

        out["DataAttributes"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_data_attributes.serialize_json(
                value["data_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartHumanLoopRequest:
    out: StartHumanLoopRequest = {}  # type: ignore[typeddict-item]
    if "HumanLoopName" in data:
        out["human_loop_name"] = data["HumanLoopName"]
    if "FlowDefinitionArn" in data:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    if "HumanLoopInput" in data:
        import capo_sagemaker_a2i_runtime.types.human_loop_input

        out["human_loop_input"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_input.deserialize_json(
                data["HumanLoopInput"]
            )
        )
    if "DataAttributes" in data:
        import capo_sagemaker_a2i_runtime.types.human_loop_data_attributes

        out["data_attributes"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_data_attributes.deserialize_json(
                data["DataAttributes"]
            )
        )
    return out
