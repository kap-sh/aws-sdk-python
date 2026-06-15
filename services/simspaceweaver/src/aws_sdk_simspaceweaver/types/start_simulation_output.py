"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StartSimulationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.sim_space_weaver_arn
    import aws_sdk_simspaceweaver.types.timestamp
    import aws_sdk_simspaceweaver.types.uuid


class StartSimulationOutput(TypedDict):
    arn: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the simulation. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    execution_id: NotRequired["aws_sdk_simspaceweaver.types.uuid.UUID"]
    """<p>A universally unique identifier (UUID) for this simulation.</p>"""
    creation_time: NotRequired["aws_sdk_simspaceweaver.types.timestamp.Timestamp"]
    """<p>The time when the simulation was created, expressed as the number of seconds and milliseconds in UTC since the Unix epoch (0:0:0.000, January 1, 1970).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSimulationOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "creation_time" in value:
        import aws_sdk_simspaceweaver.types.timestamp

        out["CreationTime"] = aws_sdk_simspaceweaver.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> StartSimulationOutput:
    out: StartSimulationOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "CreationTime" in data:
        import aws_sdk_simspaceweaver.types.timestamp

        out["creation_time"] = aws_sdk_simspaceweaver.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    return out
