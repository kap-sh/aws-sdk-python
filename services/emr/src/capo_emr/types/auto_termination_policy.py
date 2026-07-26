"""Generated from Smithy shape ``com.amazonaws.emr#AutoTerminationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.long


class AutoTerminationPolicy(TypedDict, closed=True):
    idle_timeout: NotRequired["capo_emr.types.long.Long"]
    """<p>Specifies the amount of idle time in seconds after which the cluster automatically terminates. You can specify a minimum of 60 seconds and a maximum of 604800 seconds (seven days).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoTerminationPolicy) -> dict:
    out: dict = {}
    if "idle_timeout" in value:
        out["IdleTimeout"] = value["idle_timeout"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoTerminationPolicy:
    out: AutoTerminationPolicy = {}  # type: ignore[typeddict-item]
    if "IdleTimeout" in data:
        out["idle_timeout"] = data["IdleTimeout"]
    return out
