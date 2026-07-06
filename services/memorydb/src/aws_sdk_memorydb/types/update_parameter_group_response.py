"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateParameterGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.parameter_group


class UpdateParameterGroupResponse(TypedDict, closed=True):
    parameter_group: NotRequired[
        "aws_sdk_memorydb.types.parameter_group.ParameterGroup"
    ]
    """<p>The updated parameter group</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParameterGroupResponse) -> dict:
    out: dict = {}
    if "parameter_group" in value:
        import aws_sdk_memorydb.types.parameter_group

        out["ParameterGroup"] = (
            aws_sdk_memorydb.types.parameter_group.serialize_aws_json_1_1(
                value["parameter_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateParameterGroupResponse:
    out: UpdateParameterGroupResponse = {}  # type: ignore[typeddict-item]
    if "ParameterGroup" in data:
        import aws_sdk_memorydb.types.parameter_group

        out["parameter_group"] = (
            aws_sdk_memorydb.types.parameter_group.deserialize_aws_json_1_1(
                data["ParameterGroup"]
            )
        )
    return out
