"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateAcceleratorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.accelerator


class UpdateAcceleratorResponse(TypedDict, closed=True):
    accelerator: NotRequired["capo_global_accelerator.types.accelerator.Accelerator"]
    """<p>Information about the updated accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAcceleratorResponse) -> dict:
    out: dict = {}
    if "accelerator" in value:
        import capo_global_accelerator.types.accelerator

        out["Accelerator"] = (
            capo_global_accelerator.types.accelerator.serialize_aws_json_1_1(
                value["accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAcceleratorResponse:
    out: UpdateAcceleratorResponse = {}  # type: ignore[typeddict-item]
    if "Accelerator" in data:
        import capo_global_accelerator.types.accelerator

        out["accelerator"] = (
            capo_global_accelerator.types.accelerator.deserialize_aws_json_1_1(
                data["Accelerator"]
            )
        )
    return out
