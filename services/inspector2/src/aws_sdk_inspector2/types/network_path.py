"""Generated from Smithy shape ``com.amazonaws.inspector2#NetworkPath``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.step_list


class NetworkPath(TypedDict):
    steps: NotRequired["aws_sdk_inspector2.types.step_list.StepList"]
    """<p>The details on the steps in the network path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPath) -> dict:
    out: dict = {}
    if "steps" in value:
        import aws_sdk_inspector2.types.step_list

        out["steps"] = aws_sdk_inspector2.types.step_list.serialize_json(value["steps"])
    return out


def deserialize_json(data: dict) -> NetworkPath:
    out: NetworkPath = {}  # type: ignore[typeddict-item]
    if "steps" in data:
        import aws_sdk_inspector2.types.step_list

        out["steps"] = aws_sdk_inspector2.types.step_list.deserialize_json(
            data["steps"]
        )
    return out
