"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListAcceleratorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.accelerators
    import capo_global_accelerator.types.generic_string


class ListAcceleratorsResponse(TypedDict, closed=True):
    accelerators: NotRequired["capo_global_accelerator.types.accelerators.Accelerators"]
    """<p>The list of accelerators for a customer account.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcceleratorsResponse) -> dict:
    out: dict = {}
    if "accelerators" in value:
        import capo_global_accelerator.types.accelerators

        out["Accelerators"] = (
            capo_global_accelerator.types.accelerators.serialize_aws_json_1_1(
                value["accelerators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcceleratorsResponse:
    out: ListAcceleratorsResponse = {}  # type: ignore[typeddict-item]
    if "Accelerators" in data:
        import capo_global_accelerator.types.accelerators

        out["accelerators"] = (
            capo_global_accelerator.types.accelerators.deserialize_aws_json_1_1(
                data["Accelerators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
