"""Generated from Smithy shape ``com.amazonaws.dax#UpdateParameterGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.parameter_group


class UpdateParameterGroupResponse(TypedDict, closed=True):
    parameter_group: NotRequired["capo_dax.types.parameter_group.ParameterGroup"]
    """<p>The parameter group that has been modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParameterGroupResponse) -> dict:
    out: dict = {}
    if "parameter_group" in value:
        import capo_dax.types.parameter_group

        out["ParameterGroup"] = capo_dax.types.parameter_group.serialize_aws_json_1_1(
            value["parameter_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateParameterGroupResponse:
    out: UpdateParameterGroupResponse = {}  # type: ignore[typeddict-item]
    if "ParameterGroup" in data:
        import capo_dax.types.parameter_group

        out["parameter_group"] = (
            capo_dax.types.parameter_group.deserialize_aws_json_1_1(
                data["ParameterGroup"]
            )
        )
    return out
