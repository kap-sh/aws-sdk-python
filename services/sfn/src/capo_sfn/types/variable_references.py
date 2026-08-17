"""Generated from Smithy shape ``com.amazonaws.sfn#VariableReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.state_name
    import capo_sfn.types.variable_name_list

VariableReferences: TypeAlias = dict[
    "capo_sfn.types.state_name.StateName",
    "capo_sfn.types.variable_name_list.VariableNameList",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: VariableReferences) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sfn.types.variable_name_list

        out[key] = capo_sfn.types.variable_name_list.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> VariableReferences:
    out: VariableReferences = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_sfn.types.variable_name_list

        out[key] = capo_sfn.types.variable_name_list.deserialize_aws_json_1_0(value)
    return out
