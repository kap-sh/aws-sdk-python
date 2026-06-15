"""Generated from Smithy shape ``com.amazonaws.pcs#Scheduler``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pcs.types.scheduler_type


class Scheduler(TypedDict):
    type: "aws_sdk_pcs.types.scheduler_type.SchedulerType"
    """<p>The software PCS uses to manage cluster scaling and job scheduling.</p>"""
    version: "str"
    r"""<p>The version of the specified scheduling software that PCS uses to manage cluster scaling and job scheduling. For more information, see <a href=\"https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions.html\">Slurm versions in PCS</a> in the <i>PCS User Guide</i>.</p> <p>Valid Values: <code>23.11 | 24.05 | 24.11 | 25.05 | 25.11</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Scheduler) -> dict:
    out: dict = {}
    import aws_sdk_pcs.types.scheduler_type

    out["type"] = aws_sdk_pcs.types.scheduler_type.serialize_aws_json_1_0(value["type"])
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Scheduler:
    out: Scheduler = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_pcs.types.scheduler_type

        out["type"] = aws_sdk_pcs.types.scheduler_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("Scheduler.type required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("Scheduler.version required")
    return out
